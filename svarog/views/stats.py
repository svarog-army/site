from datetime import date

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
# from flask_babel import _, get_locale

from svarog import db

from svarog import forms as f
from svarog import models as m

from svarog import schema as s
from svarog.controllers.pagination import create_pagination
from svarog.logger import log

stats_blueprint = Blueprint(
    "stats",
    __name__,
    url_prefix="/stats",
)


@stats_blueprint.route("/", methods=["GET"])
@login_required
def stats():
    period = s.Period(
        start=request.args.get("start", type=str, default=s.date_year_ago().strftime("%Y-%m-%d")),
        end=request.args.get("end", type=str, default=date.today().strftime("%Y-%m-%d")),
    )

    where = sa.and_(m.DayStats.is_deleted.is_(False), m.DayStats.day >= period.start, m.DayStats.day <= period.end)
    query = sa.select(m.DayStats).where(where).order_by(m.DayStats.created_at.desc())
    count_query = sa.select(sa.func.count()).select_from(m.DayStats).where(where)
    total = db.session.scalar(count_query)
    assert total is not None, "Total count should not be None"
    pagination = create_pagination(total=total)

    log(log.INFO, "Returning stats: [%s]", db.session.scalar(count_query))

    stats = (
        db.session.execute(query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page))
        .scalars()
        .all()
    )

    return render_template(
        "stats/stats.html",
        stats=stats,
        page=pagination,
        begin_stats_period=period.start,
        end_stats_period=period.end,
    )


@stats_blueprint.route("/get_add_form", methods=["GET"])
@login_required
def get_add_form():
    """htmx request"""
    form = f.NewStatsForm()
    return render_template("stats/add_modal.html", form=form)


# @stats_blueprint.route("/filter", methods=["POST"])
# @login_required
# def filter():
#     specialties = db.session.query(m.Specialty).filter_by(is_deleted=False).all()
#     current_lang = str(get_locale())
#     specialty_choices = [("", "All")] + [
#         (specialty.uuid, specialty.name_uk if current_lang == "uk" else specialty.name) for specialty in specialties
#     ]

#     form = f.FilterForm(specialty_choices=specialty_choices)
#     if form.validate_on_submit():
#         query_params = {
#             "q": form.search.data,
#             "status": form.status.data,
#             "specialty": form.specialty.data,
#         }
#         query_params = {key: value for key, value in query_params.items() if value}
#         return redirect(url_for("recruit.recruits", **query_params))
#     else:
#         log(log.ERROR, "Status update errors: [%s]", form.errors)
#         for key, value in form.errors.items():
#             for error in value:
#                 flash(f"{error}", "danger")
#         return redirect(request.referrer or url_for("recruit.recruits"))


# @stats_blueprint.route("/get-edit-form/<recruit_uuid>", methods=["GET"])
# @login_required
# def get_edit_form(recruit_uuid: str):
#     """htmx request"""
#     recruit: m.Recruit | None = db.session.scalar(m.Recruit.select().where(m.Recruit.uuid == recruit_uuid))

#     if not recruit or recruit.is_deleted:
#         log(log.ERROR, "Recruit not found by id: [%s]", recruit_uuid)
#         return render_template("toast.html", category="danger", message="User not found"), 404

#     if s.RecruitStatus(recruit.status) == s.RecruitStatus.APPLIED:
#         change_recruit_status(recruit, s.RecruitStatus.IN_PROGRESS)

#     form = f.RecruitForm(
#         recruit_uuid=recruit.uuid,
#         full_name=recruit.full_name,
#         birth_date=recruit.birth_date,
#         phone=recruit.phone,
#         email=recruit.email,
#         city_of_actual_residence=recruit.city_of_actual_residence,
#         education=recruit.education,
#         skills=recruit.skills,
#         last_job=recruit.last_job,
#         health_problems=recruit.health_problems,
#         have_driver_license=recruit.have_driver_license,
#         is_serviceman=recruit.is_serviceman,
#         uav_experience=recruit.uav_experience,
#         status=recruit.status.value,
#         comments=recruit.comments,
#     )

#     return render_template("recruit/edit_modal.html", form=form, recruit=recruit)


# @stats_blueprint.route("/save", methods=["POST"])
# @login_required
# def save():
#     form = f.RecruitForm()
#     if form.validate_on_submit():
#         query = m.Recruit.select().where(m.Recruit.uuid == form.recruit_uuid.data)
#         recruit: m.Recruit | None = db.session.scalar(query)
#         if not recruit:
#             log(log.ERROR, "Not found admin by id : [%s]", form.recruit_uuid.data)
#             flash(_("Cannot save user data"), "danger")
#             return redirect(url_for("admin.admins"))

#         change_recruit_status(recruit, s.RecruitStatus(form.status.data))

#         recruit.full_name = form.full_name.data
#         recruit.birth_date = form.birth_date.data
#         recruit.phone = form.phone.data
#         recruit.email = form.email.data
#         recruit.city_of_actual_residence = form.city_of_actual_residence.data
#         recruit.education = form.education.data
#         recruit.skills = form.skills.data
#         recruit.last_job = form.last_job.data
#         recruit.health_problems = form.health_problems.data
#         recruit.have_driver_license = form.have_driver_license.data
#         recruit.is_serviceman = form.is_serviceman.data
#         recruit.uav_experience = form.uav_experience.data
#         recruit.comments = form.comments.data
#         recruit.save()

#         flash(_("Recruit data updated!"), "success")

#         if form.next_url.data:
#             return redirect(form.next_url.data)
#         return redirect(url_for("recruit.recruits"))

#     else:
#         log(log.ERROR, "Recruit save errors: [%s]", form.errors)
#         for key, value in form.errors.items():
#             for error in value:
#                 flash(f"{error}", "danger")
#     return redirect(url_for("recruit.get_edit_form"))


# @stats_blueprint.route("/update_status/<recruit_uuid>", methods=["POST"])
# @login_required
# def update_status(recruit_uuid):
#     form = f.StatusForm()
#     if form.validate_on_submit():
#         query = m.Recruit.select().where(m.Recruit.uuid == recruit_uuid)
#         recruit: m.Recruit | None = db.session.scalar(query)
#         if not recruit:
#             log(log.ERROR, "Not found recruit by id: [%s]", recruit_uuid)
#             flash(_("Recruit not found"), "danger")
#             return redirect(url_for("recruit.recruits"))

#         change_recruit_status(recruit, s.RecruitStatus(form.status.data))

#         flash(_("Recruit status updated!"), "success")
#         return redirect(request.referrer or url_for("recruit.recruits"))
#     else:
#         log(log.ERROR, "Status update errors: [%s]", form.errors)
#         for key, value in form.errors.items():
#             for error in value:
#                 flash(f"{error}", "danger")
#         return redirect(request.referrer or url_for("recruit.recruits"))


# @stats_blueprint.route("/delete/<recruit_uuid>", methods=["DELETE"])
# @login_required
# def delete(recruit_uuid: str):
#     """htmx request"""
#     recruit = db.session.scalar(sa.select(m.Recruit).where(m.Recruit.uuid == recruit_uuid))
#     if not recruit or recruit.is_deleted:
#         log(log.INFO, "There is no recruit with id: [%s]", id)
#         return render_template("toast.html", category="danger", message="Recruit not found"), 404

#     datetime_now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
#     recruit.is_deleted = True
#     recruit.phone = f"deleted_{recruit.phone}_at_{datetime_now}"
#     recruit.email = f"deleted_{recruit.email}_at_{datetime_now}"
#     db.session.commit()
#     log(log.INFO, "Recruit deleted: [%s]", recruit)
#     return render_template("toast.html", category="success", message="Recruit deleted!"), 202
