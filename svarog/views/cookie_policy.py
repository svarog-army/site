from flask import (
    Blueprint,
    render_template,
)

from svarog import forms as f

cookie_policy_bp = Blueprint("cookie_policy", __name__, url_prefix="/cookie-policy")


@cookie_policy_bp.route("/", methods=["GET"])
def index():
    form = f.ApplicationForm()

    return render_template("cookie_policy.html", form=form)
