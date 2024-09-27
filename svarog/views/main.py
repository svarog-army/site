from flask import render_template, Blueprint
from config import CFG


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
def index():
    if CFG.PARKING:
        return render_template("under_construction.html")
    return render_template("index.html")


@main_blueprint.route("/no-content")
def no_content():
    """htmx request"""
    return "", 200
