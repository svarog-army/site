from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    HiddenField,
    IntegerField,
    SelectField,
    DateField,
)
from wtforms.validators import DataRequired
from flask_babel import _


class EditStatsForm(FlaskForm):
    stats_uuid = HiddenField("stats_uuid", [DataRequired()], render_kw={"readonly": True})
    tanks = IntegerField("Tanks", [DataRequired()], render_kw={"placeholder": "0"})
    mlrss = IntegerField("MLRS + SAM", [DataRequired()], render_kw={"placeholder": "0"})
    spas = IntegerField("Self-propelled artillery", [DataRequired()], render_kw={"placeholder": "0"})
    afvs = IntegerField("AFV + APC", [DataRequired()], render_kw={"placeholder": "0"})
    cars = IntegerField("Cars + trucks", [DataRequired()], render_kw={"placeholder": "0"})
    motorcycles = IntegerField("Motorcycles", [DataRequired()], render_kw={"placeholder": "0"})
    buggies = IntegerField("Buggies", [DataRequired()], render_kw={"placeholder": "0"})
    rofs = IntegerField("ROF personnel", [DataRequired()], render_kw={"placeholder": "0"})
    guns = IntegerField("Guns + howitzers", [DataRequired()], render_kw={"placeholder": "0"})
    mortars = IntegerField("Mortars", [DataRequired()], render_kw={"placeholder": "0"})
    adss = IntegerField("Air defense systems", [DataRequired()], render_kw={"placeholder": "0"})
    radars = IntegerField("EW + Radars", [DataRequired()], render_kw={"placeholder": "0"})
    ammos = IntegerField("Ammunition caches + storage facilities", [DataRequired()], render_kw={"placeholder": "0"})
    shelters = IntegerField("Shelters + dugouts", [DataRequired()], render_kw={"placeholder": "0"})
    uavs = IntegerField("Fixed-wing UAV", [DataRequired()], render_kw={"placeholder": "0"})
    antennas = IntegerField("Antennas, cameras, network equipment", [DataRequired()], render_kw={"placeholder": "0"})
    other = IntegerField("Other", [DataRequired()], render_kw={"placeholder": "0"})
    submit = SubmitField("Save")


class NewStatsForm(FlaskForm):
    """Form for creating a new statistic."""

    day = DateField(
        "Day",
        [DataRequired()],
        format="%Y-%m-%d",
    )
    stats_type = SelectField(
        "Stats Type",
        choices=[
            ("tanks", _("Tanks")),
            ("mlrss", _("MLRS + SAM")),
            ("spas", _("Self-propelled artillery")),
            ("afvs", _("AFV + APC")),
            ("cars", _("Cars + trucks")),
            ("motorcycles", _("Motorcycles")),
            ("buggies", _("Buggies")),
            ("rofs", _("ROF personnel")),
            ("guns", _("Guns + howitzers")),
            ("mortars", _("Mortars")),
            ("adss", _("Air defense systems")),
            ("radars", _("EW + Radars")),
            ("ammos", _("Ammunition caches + storage facilities")),
            ("shelters", _("Shelters + dugouts")),
            ("uavs", _("Fixed-wing UAV")),
            ("antennas", _("Antennas, cameras, network equipment")),
            ("other", _("Other")),
        ],
        validators=[DataRequired()],
    )
    count = IntegerField(_("Count"), [DataRequired()], render_kw={"placeholder": "0"})
    submit = SubmitField(_("Save"))
