from datetime import datetime

from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
)
from flask_login import login_required
import sqlalchemy as sa

from svarog import models as m, db
from svarog import forms as f
from svarog.logger import log


bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/get-edit-form/<user_uuid>", methods=["GET"])
@login_required
def get_edit_form(user_uuid: str):
    """htmx request"""
    user: m.User | None = db.session.scalar(m.User.select().where(m.User.uuid == user_uuid))
    if not user or user.is_deleted:
        log(log.ERROR, "User not found by id: [%s]", user_uuid)
        return render_template("toast.html", category="danger", message="User not found"), 404
    form = f.UserForm(
        user_uuid=user.uuid,
        email=user.email,
        username=user.username,
        activated=user.activated,
    )
    return render_template("user/edit_modal.html", form=form)


@bp.route("/save", methods=["POST"])
@login_required
def save():
    form = f.UserForm()
    if form.validate_on_submit():
        query = m.User.select().where(m.User.uuid == form.user_uuid.data)
        user: m.User | None = db.session.scalar(query)
        if not user:
            log(log.ERROR, "Not found user by id : [%s]", form.user_uuid.data)
            flash("Cannot save user data", "danger")
            return redirect(url_for("admin.get_all_users"))
        user.username = form.username.data
        user.email = form.email.data
        user.activated = form.activated.data
        if form.password.data.strip("*\n "):
            user.password = form.password.data
        user.save()
        flash("User updated!", "success")
        if form.next_url.data:
            return redirect(form.next_url.data)
        return redirect(url_for("admin.get_all_users"))

    else:
        log(log.ERROR, "User save errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.get_all_users"))


@bp.route("/get-add-form", methods=["GET"])
@login_required
def get_add_form():
    """htmx request"""
    form = f.NewUserForm()
    return render_template("user/add_modal.html", form=form)


@bp.route("/create", methods=["POST"])
@login_required
def create():
    form = f.NewUserForm()
    if form.validate_on_submit():
        user = m.User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            activated=form.activated.data,
        )
        log(log.INFO, "Form submitted. User: [%s]", user)
        flash("User added!", "success")
        user.save()
        return redirect(url_for("admin.get_all_users"))
    if form.errors:
        log(log.ERROR, "User create errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.get_all_users"))


@bp.route("/delete/<user_uuid>", methods=["DELETE"])
@login_required
def delete(user_uuid: str):
    """htmx request"""
    user = db.session.scalar(sa.select(m.User).where(m.User.uuid == user_uuid))
    if not user or user.is_deleted:
        log(log.INFO, "There is no user with id: [%s]", id)
        return render_template("toast.html", category="danger", message="User not found"), 404

    datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    user.is_deleted = True
    user.username = f"deleted_{user.username}_at_{datetime_now}"
    user.email = f"deleted_{user.email}_at_{datetime_now}"
    db.session.commit()
    log(log.INFO, "User deleted. User: [%s]", user)
    return render_template("toast.html", category="success", message="User deleted!"), 202
