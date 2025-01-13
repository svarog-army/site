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

specialty_blueprint = Blueprint(
    "specialty",
    __name__,
    url_prefix="/admin/specialty",
)


@specialty_blueprint.route("/", methods=["GET"])
@login_required
def specialties():
    if not current_user.is_admin:
        return redirect(url_for("admin.index"))
    q = request.args.get("q", type=str, default=None)
    where = m.Specialty.is_deleted.is_(False)
    if q:
        where = sa.and_(where, m.Specialty.name_uk.ilike(f"{q}%") | m.Specialty.name_en.ilike(f"{q}%"))  # type: ignore

    query = sa.select(m.Specialty).where(where).order_by(m.Specialty.id)
    count_query = sa.select(sa.func.count()).select_from(m.Specialty).where(where)
    pagination = create_pagination(total=db.session.scalar(count_query))

    log(log.INFO, "Returning specialties: [%s]", db.session.scalar(count_query))

    return render_template(
        "specialty/specialties.html",
        specialties=db.session.execute(
            query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page)
        ).scalars(),
        page=pagination,
        search_query=q,
    )


@specialty_blueprint.route("/get-edit-form/<specialty_uuid>", methods=["GET"])
@login_required
def get_edit_form(specialty_uuid: str):
    """htmx request"""
    specialty = db.session.scalar(sa.select(m.Specialty).where(m.Specialty.uuid == specialty_uuid))
    if not specialty:
        log(log.ERROR, "Specialty not found by id: [%s]", specialty_uuid)
        return render_template("toast.html", category="danger", message="Specialty not found"), 404
    form = f.SpecialtyForm(
        specialty_uuid=specialty.uuid,
        name_en=specialty.name_en,
        name_uk=specialty.name_uk,
        is_active="True" if specialty.is_active else "False",
    )
    return render_template("specialty/edit_modal.html", form=form)


@specialty_blueprint.route("/save", methods=["POST"])
@login_required
def save():
    form = f.SpecialtyForm()
    if form.validate_on_submit():
        query = m.Specialty.select().where(m.Specialty.uuid == form.specialty_uuid.data)
        specialty: m.Specialty | None = db.session.scalar(query)
        if not specialty:
            log(log.ERROR, "Not found specialty by id : [%s]", form.specialty_uuid.data)
            flash(_("Cannot save specialty data"), "danger")
            return redirect(url_for("specialty.specialties"))
        specialty.name_en = form.name_en.data
        specialty.name_uk = form.name_uk.data
        specialty.is_active = form.is_active.data == "True"
        specialty.save()
        flash(_("Specialty data updated!"), "success")
        if form.next_url.data:
            return redirect(form.next_url.data)
        return redirect(url_for("specialty.specialties"))
    elif form.errors:
        log(log.ERROR, "Specialty save errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
    return redirect(url_for("specialty.specialties"))


@specialty_blueprint.route("/get-add-form", methods=["GET"])
@login_required
def get_add_form():
    """htmx request"""
    form = f.NewSpecialtyForm()
    return render_template("specialty/add_modal.html", form=form)


@specialty_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    form: f.NewSpecialtyForm = f.NewSpecialtyForm()
    if form.validate_on_submit():
        admin = m.Specialty(
            name_en=form.name_en.data,
            name_uk=form.name_uk.data,
            is_active=form.is_active.data == "True",
        )
        admin.save()
        flash(_("Specialty created!"), "success")
        return redirect(url_for("specialty.specialties"))
    elif form.errors:
        log(log.ERROR, "Specialty create errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
    return redirect(url_for("specialty.specialties"))


@specialty_blueprint.route("/delete/<specialty_uuid>", methods=["DELETE"])
@login_required
def delete(specialty_uuid: str):
    """htmx request"""
    specialty = db.session.scalar(sa.select(m.Specialty).where(m.Specialty.uuid == specialty_uuid))
    if not specialty or specialty.is_deleted:
        log(log.INFO, "There is no specialty with id: [%s]", id)
        return render_template("toast.html", category="danger", message="Specialty not found"), 404
    # check if specialty is used in any application
    if specialty.applications:
        log(log.INFO, "Specialty is used in applications: [%s]", specialty)
        return render_template("toast.html", category="danger", message="Specialty is used in applications"), 400
    datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    specialty.is_deleted = True
    specialty.name_en = f"deleted_{specialty.name_en}_at_{datetime_now}"
    specialty.name_uk = f"deleted_{specialty.name_uk}_at_{datetime_now}"
    db.session.commit()
    log(log.INFO, "Specialty deleted: [%s]", specialty)
    return render_template("toast.html", category="success", message="Specialty deleted!"), 202
