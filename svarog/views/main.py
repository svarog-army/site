from flask import Blueprint, request, redirect, g, current_app, url_for, abort
from config import CFG


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/no-content")
def no_content():
    """htmx request"""
    return "", 200


@main_blueprint.route("/change-locale", methods=["POST"])
def change_locale():
    """get current locale from and save it to session"""
    locale = request.form.get("locale")
    if locale in CFG.BABEL_SUPPORTED_LOCALES:
        g.lang_code = locale
    else:
        g.lang_code = CFG.BABEL_DEFAULT_LOCALE

    adapter = current_app.url_map.bind("")
    try:
        # URL referrer without domain name and protocol
        relative_url = request.referrer.replace(request.url_root, "")
        endpoint, args = adapter.match(relative_url)
        args["lang_code"] = g.lang_code  # type: ignore
        return redirect(url_for(endpoint, **args))
    except Exception:
        abort(404)
