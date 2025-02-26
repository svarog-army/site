from flask import Blueprint, request, redirect, g, current_app, url_for, abort
from config import CFG
from svarog.logger import log


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/no-content")
def no_content():
    """HTMX request"""
    return "", 200


@main_blueprint.route("/change-locale", methods=["POST"])
def change_locale():
    """get current locale from and save it to session"""
    locale = request.form.get("locale")
    if locale in CFG.BABEL_SUPPORTED_LOCALES:
        g.lang_code = locale
    else:
        g.lang_code = CFG.BABEL_DEFAULT_LOCALE

    log(log.INFO, "change_locale: g.lang_code: [%s]", g.lang_code)

    adapter = current_app.url_map.bind("")
    try:
        # URL referrer without domain name and protocol
        url_root = request.url_root
        relative_url = request.referrer.replace(url_root, "")
        url_root = url_root.replace("http://", "https://")
        relative_url = relative_url.replace(url_root, "")
        log(log.INFO, "change_locale: relative_url: [%s]", relative_url)
        endpoint, args = adapter.match(relative_url)
        args["lang_code"] = g.lang_code  # type: ignore
        return redirect(url_for(endpoint, **args), code=301)
    except Exception as e:
        log(log.ERROR, "Failed to change locale: %s", e)
        abort(404)
