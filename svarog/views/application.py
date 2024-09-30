import sqlalchemy as sa
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from flask_babel import _

from svarog import db
from svarog import forms as f
from svarog import models as m
from svarog.logger import log

application_bp = Blueprint("application", __name__, url_prefix="/application")


@application_bp.route("/get-application-form", methods=["GET"])
def get_application_form():
    """htmx request"""
    form = f.ApplicationForm()
    specialties = db.session.scalars(sa.select(m.Specialty)).all()
    return render_template("application_modal.html", form=form, specialties=specialties)


@application_bp.route("/create", methods=["POST"])
def create():
    form: f.ApplicationForm = f.ApplicationForm()
    if not form.validate_on_submit():
        log(log.ERROR, "Application create errors: [%s]", form.errors)
        return {"status": "error", "message": f"{form.errors}"}, 400
    application = m.Application(
        full_name=form.full_name.data,
        birth_date=form.birth_date.data,
        phone=form.phone.data,
        email=form.email.data,
        city_of_actual_residence=form.city_of_actual_residence.data,
        education=form.education.data,
        skills=form.skills.data,
        last_job=form.last_job.data,
        health_problems=form.health_problems.data,
        have_driver_license=form.have_driver_license.data,
        is_serviceman=True if form.is_serviceman.data == "yes" else False,
        uav_experience=form.uav_experience.data,
        specialties=form.applied_specialties.data,
    )
    existing_recruit = db.session.scalar(sa.select(m.Recruit).where(m.Recruit.phone == form.phone.data))
    if existing_recruit:
        application.recruit_id = existing_recruit.id
        existing_recruit.applications.extend(application.applied_specialties)
    else:
        recruit = m.Recruit(
            full_name=form.full_name.data,
            birth_date=form.birth_date.data,
            phone=form.phone.data,
            email=form.email.data,
            city_of_actual_residence=form.city_of_actual_residence.data,
            education=form.education.data,
            skills=form.skills.data,
            last_job=form.last_job.data,
            health_problems=form.health_problems.data,
            have_driver_license=form.have_driver_license.data,
            is_serviceman=True if form.is_serviceman.data == "yes" else False,
            uav_experience=form.uav_experience.data,
        )
        recruit.save()
        application.recruit_id = recruit.id

    log(log.INFO, "Form submitted. Application: [%s]", application)
    application.save()
    flash(_("Application applied successfully"), "success")
    return redirect(url_for("home"))
