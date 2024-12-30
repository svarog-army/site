from datetime import datetime

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from flask_babel import _

from svarog import db
from svarog import forms as f
from svarog import models as m
from svarog.controllers.pagination import create_pagination
from svarog.logger import log

recruit_blueprint = Blueprint(
    "recruit",
    __name__,
    url_prefix="/admin/recruit",
)


@recruit_blueprint.route("/", methods=["GET"])
@login_required
def recruits():
    q = request.args.get("q", type=str, default=None)
    where = m.Recruit.is_deleted.is_(False)
    if q:
        where = sa.and_(where, m.Recruit.full_name.ilike(f"{q}%") | m.Recruit.phone.ilike(f"{q}%"))  # type: ignore

    query = sa.select(m.Recruit).where(where).order_by(m.Recruit.created_at.desc())
    count_query = sa.select(sa.func.count()).select_from(m.Recruit).where(where)
    pagination = create_pagination(total=db.session.scalar(count_query))

    log(log.INFO, "Returning recruits: [%s]", db.session.scalar(count_query))

    recruits = (
        db.session.execute(query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page))
        .scalars()
        .all()
    )

    recruit_forms = {}

    for recruit in recruits:
        form = f.StatusForm(status=recruit.status.value)
        recruit_forms[recruit.uuid] = form

    return render_template(
        "recruit/recruits.html",
        recruits=recruits,
        page=pagination,
        search_query=q,
        recruit_forms=recruit_forms,
    )


@recruit_blueprint.route("/get-edit-form/<recruit_uuid>", methods=["GET"])
@login_required
def get_edit_form(recruit_uuid: str):
    """htmx request"""
    recruit: m.Recruit | None = db.session.scalar(m.Recruit.select().where(m.Recruit.uuid == recruit_uuid))
    if not recruit or recruit.is_deleted:
        log(log.ERROR, "Recruit not found by id: [%s]", recruit_uuid)
        return render_template("toast.html", category="danger", message="User not found"), 404
    form = f.RecruitForm(
        recruit_uuid=recruit.uuid,
        full_name=recruit.full_name,
        birth_date=recruit.birth_date,
        phone=recruit.phone,
        email=recruit.email,
        city_of_actual_residence=recruit.city_of_actual_residence,
        education=recruit.education,
        skills=recruit.skills,
        last_job=recruit.last_job,
        health_problems=recruit.health_problems,
        have_driver_license=recruit.have_driver_license,
        is_serviceman=recruit.is_serviceman,
        uav_experience=recruit.uav_experience,
        status=recruit.status,
        comments=recruit.comments,
    )
    return render_template("recruit/edit_modal.html", form=form)


@recruit_blueprint.route("/save", methods=["POST"])
@login_required
def save():
    form = f.RecruitForm()
    if form.validate_on_submit():
        query = m.Recruit.select().where(m.Recruit.uuid == form.recruit_uuid.data)
        recruit: m.Recruit | None = db.session.scalar(query)
        if not recruit:
            log(log.ERROR, "Not found admin by id : [%s]", form.recruit_uuid.data)
            flash(_("Cannot save user data"), "danger")
            return redirect(url_for("admin.admins"))
        recruit.full_name = form.full_name.data
        recruit.birth_date = form.birth_date.data
        recruit.phone = form.phone.data
        recruit.email = form.email.data
        recruit.city_of_actual_residence = form.city_of_actual_residence.data
        recruit.education = form.education.data
        recruit.skills = form.skills.data
        recruit.last_job = form.last_job.data
        recruit.health_problems = form.health_problems.data
        recruit.have_driver_license = form.have_driver_license.data
        recruit.is_serviceman = form.is_serviceman.data
        recruit.uav_experience = form.uav_experience.data
        recruit.status = form.status.data
        recruit.comments = form.comments.data
        recruit.save()
        flash(_("Recruit data updated!"), "success")
        if form.next_url.data:
            return redirect(form.next_url.data)
        return redirect(url_for("recruit.recruits"))

    else:
        log(log.ERROR, "Recruit save errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
    return redirect(url_for("recruit.get_edit_form"))


@recruit_blueprint.route("/update_status/<recruit_uuid>", methods=["POST"])
@login_required
def update_status(recruit_uuid):
    form = f.StatusForm()
    if form.validate_on_submit():
        query = m.Recruit.select().where(m.Recruit.uuid == recruit_uuid)
        recruit: m.Recruit | None = db.session.scalar(query)
        if not recruit:
            log(log.ERROR, "Not found recruit by id: [%s]", recruit_uuid)
            flash(_("Recruit not found"), "danger")
            return redirect(url_for("recruit.recruits"))

        recruit.status = form.status.data
        recruit.save()

        flash(_("Recruit status updated!"), "success")
        return redirect(request.referrer or url_for("recruit.recruits"))
    else:
        log(log.ERROR, "Status update errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
        return redirect(request.referrer or url_for("recruit.recruits"))


@recruit_blueprint.route("/delete/<recruit_uuid>", methods=["DELETE"])
@login_required
def delete(recruit_uuid: str):
    """htmx request"""
    recruit = db.session.scalar(sa.select(m.Recruit).where(m.Recruit.uuid == recruit_uuid))
    if not recruit or recruit.is_deleted:
        log(log.INFO, "There is no recruit with id: [%s]", id)
        return render_template("toast.html", category="danger", message="Recruit not found"), 404

    datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    recruit.is_deleted = True
    recruit.phone = f"deleted_{recruit.phone}_at_{datetime_now}"
    recruit.email = f"deleted_{recruit.email}_at_{datetime_now}"
    db.session.commit()
    log(log.INFO, "Recruit deleted: [%s]", recruit)
    return render_template("toast.html", category="success", message="Recruit deleted!"), 202
