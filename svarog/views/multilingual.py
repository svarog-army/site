from datetime import date, timedelta
import sqlalchemy as sa
from flask import Blueprint, abort, current_app, g, redirect, render_template, request, url_for
from flask_wtf import FlaskForm

from config import CFG
from svarog import db
from svarog import forms as f
from svarog import models as m
from svarog import schema as s

multilingual = Blueprint("multilingual", __name__, template_folder="templates", url_prefix="/<lang_code>")

SERVICE_ROUTES = ["admin", "auth", "favicon.ico", "static"]


@multilingual.url_defaults
def add_language_code(endpoint, values):
    values.setdefault("lang_code", g.lang_code)


@multilingual.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop("lang_code")


@multilingual.before_request
def before_request():
    if g.lang_code not in CFG.BABEL_SUPPORTED_LOCALES:
        adapter = current_app.url_map.bind("")
        try:
            endpoint, args = adapter.match("/uk" + request.full_path.rstrip("/ ?"))
            return redirect(url_for(endpoint, **args), code=301)
        except Exception:
            abort(404)

    dfl = request.url_rule.defaults if request.url_rule else None
    if dfl and "lang_code" in dfl:
        if dfl["lang_code"] != request.full_path.split("/")[1]:
            abort(404)


@multilingual.route("/")
def index():
    if CFG.PARKING:
        return render_template("under_construction.html", form=FlaskForm())

    form = f.ApplicationForm()
    specialties = db.session.scalars(sa.select(m.Specialty)).all()

    return render_template("index.html", form=FlaskForm(), application_form=form, specialties=specialties)


@multilingual.route("/stats/")
def stats():
    period = request.args.get("period", type=str, default="day")
    start_day = date.today() - timedelta(days=1)
    if period == "week":
        start_day = date.today() - timedelta(days=7)
    elif period == "month":
        start_day = date.today() - timedelta(days=31)

    if period == "day":
        stats = m.DayStats.last_day()
    else:
        stats = m.DayStats.get_stats_for_period(s.Period(start=start_day, end=date.today()))

    return render_template("stats.html", form=FlaskForm(), stats=stats, period=period, start_day=start_day)


@multilingual.route("/cookie_policy/", methods=["GET"])
def cookie_policy():
    form = f.ApplicationForm()
    return render_template("cookie_policy.html", form=form)


@multilingual.route("/privacy_policy/", methods=["GET"])
def privacy_policy():
    form = f.ApplicationForm()
    return render_template("privacy_policy.html", form=form)
