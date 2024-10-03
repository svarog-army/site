from flask import (
    Blueprint,
    g,
    render_template,
    request,
)

from config import CFG
from svarog import forms as f

cookie_policy_bp = Blueprint("cookie_policy", __name__, url_prefix="/cookie-policy")



@cookie_policy_bp.route("/<string(length=2):lang_code>/", methods=["GET"])
def index(lang_code):
    form = f.ApplicationForm()
    locale = request.form.get("locale")
    if locale in CFG.BABEL_SUPPORTED_LOCALES:
        g.lang_code = locale
    else:
        g.lang_code = lang_code


    return render_template("cookie_policy.html", form=form, lang_code=locale)
