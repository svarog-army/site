from datetime import datetime

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required

from svarog import db
from svarog import forms as f
from svarog import models as m
from svarog.controllers.pagination import create_pagination
from svarog.logger import log

admin_blueprint = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin",
)


@admin_blueprint.route("/", methods=["GET"])
@login_required
def index():
    return redirect(url_for("admin.get_all_admins"))


@admin_blueprint.route("/admins", methods=["GET"])
@login_required
def get_all_admins():
    q = request.args.get("q", type=str, default=None)
    where = m.User.is_deleted.is_(False) & m.User.is_admin.is_(True)
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
    form = f.AdminForm(
        admin_uuid=admin.uuid,
        email=admin.email,
        username=admin.username,
        activated=admin.activated,
    )
    return render_template("admin/edit_modal.html", form=form)


@admin_blueprint.route("/save", methods=["POST"])
@login_required
def save():
    form: f.AdminForm = f.AdminForm()
    if form.validate_on_submit():
        query = m.User.select().where(m.User.uuid == form.admin_uuid.data)
        admin: m.User | None = db.session.scalar(query)
        if not admin:
            log(log.ERROR, "Not found admin by id : [%s]", form.admin_uuid.data)
            flash("Cannot save admin data", "danger")
            return redirect(url_for("admin.get_all_admins"))
        admin.username = form.username.data
        admin.email = form.email.data
        admin.activated = form.activated.data
        if form.password.data.strip("*\n "):
            admin.password = form.password.data
        admin.save()
        flash("Admin updated!", "success")
        if form.next_url.data:
            return redirect(form.next_url.data)
        return redirect(url_for("admin.get_all_admins"))

    else:
        log(log.ERROR, "Admin save errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.get_all_users"))


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
            is_admin=True,
            password=form.password.data,
            activated=form.activated.data,
        )
        log(log.INFO, "Form submitted. Admin: [%s]", admin)
        flash("Admin added!", "success")
        admin.save()
        return redirect(url_for("admin.get_all_admins"))
    if form.errors:
        log(log.ERROR, "Admin create errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.get_all_admins"))


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
    log(log.INFO, "Admin deleted. Admin: [%s]", admin)
    return render_template("toast.html", category="success", message="User deleted!"), 202


@admin_blueprint.route("/users", methods=["GET"])
@login_required
def get_all_users():
    q = request.args.get("q", type=str, default=None)
    where = m.User.is_deleted.is_(False) & m.User.is_admin.is_(False)
    if q:
        where = sa.and_(where, m.User.username.ilike(f"{q}%") | m.User.email.ilike(f"{q}%"))  # type: ignore

    query = sa.select(m.User).where(where).order_by(m.User.id)
    count_query = sa.select(sa.func.count()).select_from(m.User).where(where)
    pagination = create_pagination(total=db.session.scalar(count_query))

    log(log.INFO, "Returning users: [%s]", db.session.scalar(count_query))

    return render_template(
        "user/users.html",
        users=db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page)
        ).scalars(),
        page=pagination,
        search_query=q,
    )
