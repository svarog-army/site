from datetime import date

import sqlalchemy as sa
from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_required
from flask_babel import _

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
        start=request.args.get("start", type=str, default=s.date_year_ago().strftime("%Y-%m-%d")),  # type: ignore
        end=request.args.get("end", type=str, default=date.today().strftime("%Y-%m-%d")),  # type: ignore
    )

    where = sa.and_(m.DayStats.is_deleted.is_(False), m.DayStats.day >= period.start, m.DayStats.day <= period.end)
    query = sa.select(m.DayStats).where(where).order_by(m.DayStats.created_at.desc())
    count_query = sa.select(sa.func.count()).select_from(m.DayStats).where(where)
    total = db.session.scalar(count_query)  # type: ignore
    assert total is not None, "Total count should not be None"
    pagination = create_pagination(total=total)

    log(log.INFO, "Returning stats: [%s]", db.session.scalar(count_query))  # type: ignore

    stats = (
        db.session.execute(query.offset((pagination.page - 1) * pagination.per_page).limit(pagination.per_page))  # type: ignore
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
    day = session.get("day", date.today())
    # if day is type of str, convert it to date
    if isinstance(day, str):
        day = date.fromisoformat(day)
    form.day.data = day
    form.stats_type.data = session.get("stats_type", "rofs")
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


@stats_blueprint.route("/get-edit-form/<stat_uuid>", methods=["GET"])
@login_required
def get_edit_form(stat_uuid: str):
    """htmx request"""
    stats: m.DayStats | None = db.session.scalar(m.DayStats.select().where(m.DayStats.uuid == stat_uuid))  # type: ignore

    if not stats or stats.is_deleted:
        log(log.ERROR, "Day Statistics not found by id: [%s]", stat_uuid)
        return render_template("toast.html", category="danger", message="Day Statistics not found"), 404

    form = f.EditStatsForm()
    form.tanks.data = stats.tanks
    form.tanks_destroyed.data = stats.tanks_destroyed
    form.mlrss.data = stats.mlrss
    form.mlrss_destroyed.data = stats.mlrss_destroyed
    form.spas.data = stats.spas
    form.spas_destroyed.data = stats.spas_destroyed
    form.afvs.data = stats.afvs
    form.afvs_destroyed.data = stats.afvs_destroyed
    form.cars.data = stats.cars
    form.cars_destroyed.data = stats.cars_destroyed
    form.motorcycles.data = stats.motorcycles
    form.motorcycles_destroyed.data = stats.motorcycles_destroyed
    form.buggies.data = stats.buggies
    form.buggies_destroyed.data = stats.buggies_destroyed
    form.rofs.data = stats.rofs
    form.rofs_destroyed.data = stats.rofs_destroyed
    form.guns.data = stats.guns
    form.guns_destroyed.data = stats.guns_destroyed
    form.mortars.data = stats.mortars
    form.mortars_destroyed.data = stats.mortars_destroyed
    form.adss.data = stats.adss
    form.adss_destroyed.data = stats.adss_destroyed
    form.radars.data = stats.radars
    form.radars_destroyed.data = stats.radars_destroyed
    form.ammos.data = stats.ammos
    form.ammos_destroyed.data = stats.ammos_destroyed
    form.shelters.data = stats.shelters
    form.shelters_destroyed.data = stats.shelters_destroyed
    form.uavs.data = stats.uavs
    form.uavs_destroyed.data = stats.uavs_destroyed
    form.antennas.data = stats.antennas
    form.antennas_destroyed.data = stats.antennas_destroyed
    form.other.data = stats.other
    form.other_destroyed.data = stats.other_destroyed
    form.impact_flights.data = stats.impact_flights
    form.scouting_flights.data = stats.scouting_flights
    form.found_targets.data = stats.found_targets
    form.found_fpv_drones.data = stats.found_fpv_drones
    form.destroyed_fpv_drones.data = stats.destroyed_fpv_drones
    form.mining_flights.data = stats.mining_flights
    form.setup_mines.data = stats.setup_mines
    form.stats_uuid.data = stat_uuid

    return render_template("stats/edit_modal.html", form=form)


@stats_blueprint.route("/save", methods=["POST"])
@login_required
def save():
    form = f.EditStatsForm()
    if form.validate_on_submit():
        query = m.DayStats.select().where(m.DayStats.uuid == form.stats_uuid.data)
        stats: m.DayStats | None = db.session.scalar(query)  # type: ignore
        if not stats:
            log(log.ERROR, "Not found day statistics by id : [%s]", form.stats_uuid.data)
            flash(_("Cannot update day statistics data"), "danger")
            return redirect(url_for("admin.stats.stats"))

        stats.tanks = form.tanks.data
        stats.tanks_destroyed = form.tanks_destroyed.data
        stats.mlrss = form.mlrss.data
        stats.mlrss_destroyed = form.mlrss_destroyed.data
        stats.spas = form.spas.data
        stats.spas_destroyed = form.spas_destroyed.data
        stats.afvs = form.afvs.data
        stats.afvs_destroyed = form.afvs_destroyed.data
        stats.cars = form.cars.data
        stats.cars_destroyed = form.cars_destroyed.data
        stats.motorcycles = form.motorcycles.data
        stats.motorcycles_destroyed = form.motorcycles_destroyed.data
        stats.buggies = form.buggies.data
        stats.buggies_destroyed = form.buggies_destroyed.data
        stats.rofs = form.rofs.data
        stats.rofs_destroyed = form.rofs_destroyed.data
        stats.guns = form.guns.data
        stats.guns_destroyed = form.guns_destroyed.data
        stats.mortars = form.mortars.data
        stats.mortars_destroyed = form.mortars_destroyed.data
        stats.adss = form.adss.data
        stats.adss_destroyed = form.adss_destroyed.data
        stats.radars = form.radars.data
        stats.radars_destroyed = form.radars_destroyed.data
        stats.ammos = form.ammos.data
        stats.ammos_destroyed = form.ammos_destroyed.data
        stats.shelters = form.shelters.data
        stats.shelters_destroyed = form.shelters_destroyed.data
        stats.uavs = form.uavs.data
        stats.uavs_destroyed = form.uavs_destroyed.data
        stats.antennas = form.antennas.data
        stats.antennas_destroyed = form.antennas_destroyed.data
        stats.other = form.other.data
        stats.other_destroyed = form.other_destroyed.data
        stats.impact_flights = form.impact_flights.data
        stats.scouting_flights = form.scouting_flights.data
        stats.found_targets = form.found_targets.data
        stats.found_fpv_drones = form.found_fpv_drones.data
        stats.destroyed_fpv_drones = form.destroyed_fpv_drones.data
        stats.mining_flights = form.mining_flights.data
        stats.setup_mines = form.setup_mines.data
        stats.save()

        flash(_("Day Statistics data updated!"), "success")

        return redirect(url_for("admin.stats.stats"))

    else:
        log(log.ERROR, "Day Statistics save errors: [%s]", form.errors)
        for key, value in form.errors.items():
            for error in value:
                flash(f"{error}", "danger")
    return redirect(url_for("admin.stats.stats"))


@stats_blueprint.route("/delete/<stats_uuid>", methods=["DELETE"])
@login_required
def delete(stats_uuid: str):
    """htmx request"""
    stats = db.session.scalar(sa.select(m.DayStats).where(m.DayStats.uuid == stats_uuid))  # type: ignore
    if not stats or stats.is_deleted:
        log(log.ERROR, "There is no day statistics with id: [%s]", stats_uuid)
        return render_template("toast.html", category="danger", message=_("Day Statistic not found")), 404

    stats.is_deleted = True
    db.session.commit()  # type: ignore
    log(log.INFO, "Day Statistics deleted: [%s]", stats_uuid)
    # return render_template("toast.html", category="success", message="Recruit deleted!"), 202
    return redirect(url_for("admin.stats.stats"))


@stats_blueprint.route("/create", methods=["POST"])
@login_required
def create():
    form: f.NewStatsForm = f.NewStatsForm()
    if form.validate_on_submit():
        assert form.day.data is not None, "Day should not be None"
        session["day"] = form.day.data.isoformat()
        session["stats_type"] = form.stats_type.data
        # check if stats record for this day already exists
        # if it does not, create a new one
        stats = db.session.scalar(  # type: ignore
            sa.select(m.DayStats).where(
                sa.and_(
                    m.DayStats.day == form.day.data,
                    m.DayStats.is_deleted.is_(False),
                )
            )
        )
        if not stats:
            stats = m.DayStats(day=form.day.data)
        else:
            if stats.get_value_by_name(form.stats_type.data) is not None:
                flash(_("Stats for this day already exists! Please edit or delete it"), "danger")
                return redirect(url_for("admin.stats.stats"))

        # set the value for the stats type
        assert form.count.data is not None, "Count should not be None"
        stats.set_value_by_name(form.stats_type.data, form.count.data, form.count_destroyed.data)
        stats.save()
        log(log.INFO, "Form day statistic submitted. Stats: [%s] value: [%s]", form.stats_type.data, form.count.data)

        flash(_("Day statistic added!"), "success")
    if form.errors:
        log(log.ERROR, "Adding statistic errors: [%s]", form.errors)
        flash(f"{form.errors}", "danger")

    return redirect(url_for("admin.stats.stats"))
