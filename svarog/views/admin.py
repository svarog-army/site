from datetime import datetime

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from flask_babel import _

from svarog import db
from svarog import forms as f
from svarog import models as m
from svarog.controllers.pagination import create_pagination
from svarog.logger import log
from .stats import stats_blueprint

admin_blueprint = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)
# Register the stats blueprint to the admin blueprint
admin_blueprint.register_blueprint(stats_blueprint)

BLANK_PASSWORD = "********"


@admin_blueprint.route("/", methods=["GET"])
@login_required
def index():
    if current_user.is_admin:
        return redirect(url_for("admin.admins"))
    return redirect(url_for("recruit.recruits"))


@admin_blueprint.route("/admins", methods=["GET"])
@login_required
def admins():
    if not current_user.is_admin:
        return redirect(url_for("admin.index"))
    q = request.args.get("q", type=str, default=None)
    where = m.User.is_deleted.is_(False)
    if q:
        where = sa.and_(where, m.User.username.ilike(f"{q}%") | m.User.email.ilike(f"{q}%"))  # type: ignore

    query = sa.select(m.User).where(where).order_by(m.User.id)
    count_query = sa.select(sa.func.count()).select_from(m.User).where(where)
    pagination = create_pagination(total=db.session.scalar(count_query))

    log(log.INFO, "Returning admins: [%s]", db.session.scalar(count_query))

    return render_template(
        "admin/admins.html",
        admins=db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page)
        ).scalars(),
        page=pagination,
        search_query=q,
    )


@admin_blueprint.route("/get-edit-form/<admin_uuid>", methods=["GET"])
@login_required
def get_edit_form(admin_uuid: str):
    """htmx request"""
    admin: m.User | None = db.session.scalar(m.User.select().where(m.User.uuid == admin_uuid))
    if not admin or admin.is_deleted:
        log(log.ERROR, "Admin not found by id: [%s]", admin_uuid)
        return render_template("toast.html", category="danger", message="User not found"), 404
    form = f.UserForm(
        user_uuid=admin.uuid,
        email=admin.email,
        username=admin.username,
        is_admin=admin.is_admin,
        password=BLANK_PASSWORD,
        password_confirmation=BLANK_PASSWORD,
    )
    form.password.data = BLANK_PASSWORD
    form.password_confirmation.data = BLANK_PASSWORD
    return render_template("admin/edit_modal.html", form=form)


@admin_blueprint.route("/save", methods=["POST"])
@login_required
def save():
    form = f.UserForm()
    if form.validate_on_submit():
        query = m.User.select().where(m.User.uuid == form.user_uuid.data)
        admin: m.User | None = db.session.scalar(query)
        if not admin:
            log(log.ERROR, "Not found admin by id : [%s]", form.user_uuid.data)
            flash(_("Cannot save user data"), "danger")
            return redirect(url_for("admin.admins"))
        admin.username = form.username.data
        admin.email = form.email.data
        admin.activated = True
        admin.is_admin = form.is_admin.data
        if form.password.data.strip("*\n "):
            admin.password = form.password.data
        admin.save()
        flash(_("User updated!"), "success")
        if form.next_url.data:
            return redirect(form.next_url.data)
        return redirect(url_for("admin.admins"))

    else:
        log(log.ERROR, "Admin save errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
    return redirect(url_for("admin.admins"))


@admin_blueprint.route("/get-add-form", methods=["GET"])
@login_required
def get_add_form():
    """htmx request"""
    form = f.NewUserForm()
    return render_template("admin/add_modal.html", form=form)


@admin_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    form: f.NewUserForm = f.NewUserForm()
    if form.validate_on_submit():
        admin = m.User(
            username=form.username.data,
            email=form.email.data,
            is_admin=form.is_admin.data,
            password=form.password.data,
            activated=True,
        )
        log(log.INFO, "Form submitted. Admin: [%s]", admin)
        flash(_("User added!"), "success")
        admin.save()
        return redirect(url_for("admin.admins"))
    if form.errors:
        log(log.ERROR, "User create errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.admins"))


@admin_blueprint.route("/delete/<admin_uuid>", methods=["DELETE"])
@login_required
def delete(admin_uuid: str):
    """htmx request"""
    admin = db.session.scalar(sa.select(m.User).where(m.User.uuid == admin_uuid))
    if not admin or admin.is_deleted:
        log(log.INFO, "There is no admin with id: [%s]", id)
        return render_template("toast.html", category="danger", message="Admin not found"), 404

    datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    admin.is_deleted = True
    admin.username = f"deleted_{admin.username}_at_{datetime_now}"
    admin.email = f"deleted_{admin.email}_at_{datetime_now}"
    db.session.commit()
    log(log.INFO, "User deleted. User: [%s]", admin)
    return render_template("toast.html", category="success", message="User deleted!"), 202
