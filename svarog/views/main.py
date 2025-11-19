from flask import Blueprint, request, redirect, g, current_app, url_for, abort, render_template
from flask_wtf import FlaskForm
from config import CFG
from svarog.logger import log
from svarog.controllers import get_custom_links


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/no-content")
def no_content():
    """HTMX request"""
    return "", 200


@main_blueprint.before_request
def before_request():
    g.custom_links = get_custom_links()


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


@main_blueprint.route("/test-drive/", methods=["GET"])
def test_drive():
    links = get_custom_links()
    form = FlaskForm()
    # Redirect to the test drive link if set
    if links.test_drive:
        # return redirect(links.test_drive)
        return render_template("redirect.html", redirect_url=links.test_drive, form=form)
    else:
        abort(404)
