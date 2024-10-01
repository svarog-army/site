from flask import render_template, Blueprint, g, redirect, request, current_app, abort, url_for
from flask_wtf import FlaskForm

from config import CFG

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
            return redirect(url_for(endpoint, **args), 301)
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

    return render_template("index.html", form=FlaskForm())
