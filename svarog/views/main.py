from flask import render_template, Blueprint, request, session, redirect
from flask_babel import gettext
from config import CFG
from svarog.logger import log


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    if CFG.PARKING:
        return render_template("under_construction.html")
    hello = gettext("привіт")
    log(log.INFO, hello)

    return render_template("index.html")


@main_blueprint.route("/no-content")
def no_content():
    """htmx request"""
    return "", 200


@main_blueprint.route("/change-locale", methods=["POST"])
def change_locale():
    """get current locale from and save it to session"""
    locale = request.form.get("locale")
    if locale in CFG.BABEL_SUPPORTED_LOCALES:
        session["locale"] = locale
    return redirect(request.referrer)
