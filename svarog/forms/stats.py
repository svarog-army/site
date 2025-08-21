from flask_wtf import FlaskForm
from wtforms import (
    SubmitField,
    HiddenField,
    IntegerField,
    SelectField,
    DateField,
)
from wtforms.validators import DataRequired, InputRequired, Optional
from flask_babel import _


class EditStatsForm(FlaskForm):
    stats_uuid = HiddenField("stats_uuid", [DataRequired()], render_kw={"readonly": True})
    tanks = IntegerField("Tanks", [Optional()], render_kw={"placeholder": "0"})
    tanks_destroyed = IntegerField("Tanks Destroyed", [Optional()], render_kw={"placeholder": "0"})
    mlrss = IntegerField("MLRS + SAM", [Optional()], render_kw={"placeholder": "0"})
    mlrss_destroyed = IntegerField("MLRS + SAM Destroyed", [Optional()], render_kw={"placeholder": "0"})
    spas = IntegerField("Self-propelled artillery", [Optional()], render_kw={"placeholder": "0"})
    spas_destroyed = IntegerField("Self-propelled artillery Destroyed", [Optional()], render_kw={"placeholder": "0"})
    afvs = IntegerField("AFV + APC", [Optional()], render_kw={"placeholder": "0"})
    afvs_destroyed = IntegerField("AFV + APC Destroyed", [Optional()], render_kw={"placeholder": "0"})
    cars = IntegerField("Cars + trucks", [Optional()], render_kw={"placeholder": "0"})
    cars_destroyed = IntegerField("Cars + trucks Destroyed", [Optional()], render_kw={"placeholder": "0"})
    motorcycles = IntegerField("Motorcycles", [Optional()], render_kw={"placeholder": "0"})
    motorcycles_destroyed = IntegerField("Motorcycles Destroyed", [Optional()], render_kw={"placeholder": "0"})
    buggies = IntegerField("Buggies", [Optional()], render_kw={"placeholder": "0"})
    buggies_destroyed = IntegerField("Buggies Destroyed", [Optional()], render_kw={"placeholder": "0"})
    rofs = IntegerField("ROF personnel", [Optional()], render_kw={"placeholder": "0"})
    rofs_destroyed = IntegerField("ROF personnel Destroyed", [Optional()], render_kw={"placeholder": "0"})
    guns = IntegerField("Guns + howitzers", [Optional()], render_kw={"placeholder": "0"})
    guns_destroyed = IntegerField("Guns + howitzers Destroyed", [Optional()], render_kw={"placeholder": "0"})
    mortars = IntegerField("Mortars", [Optional()], render_kw={"placeholder": "0"})
    mortars_destroyed = IntegerField("Mortars Destroyed", [Optional()], render_kw={"placeholder": "0"})
    adss = IntegerField("Air defense systems", [Optional()], render_kw={"placeholder": "0"})
    adss_destroyed = IntegerField("Air defense systems Destroyed", [Optional()], render_kw={"placeholder": "0"})
    radars = IntegerField("EW + Radars", [Optional()], render_kw={"placeholder": "0"})
    radars_destroyed = IntegerField("EW + Radars Destroyed", [Optional()], render_kw={"placeholder": "0"})
    ammos = IntegerField("Ammunition caches + storage facilities", [Optional()], render_kw={"placeholder": "0"})
    ammos_destroyed = IntegerField(
        "Ammunition caches + storage facilities Destroyed", [Optional()], render_kw={"placeholder": "0"}
    )
    shelters = IntegerField("Shelters + dugouts", [Optional()], render_kw={"placeholder": "0"})
    shelters_destroyed = IntegerField("Shelters + dugouts Destroyed", [Optional()], render_kw={"placeholder": "0"})
    uavs = IntegerField("Fixed-wing UAV", [Optional()], render_kw={"placeholder": "0"})
    uavs_destroyed = IntegerField("Fixed-wing UAV Destroyed", [Optional()], render_kw={"placeholder": "0"})
    antennas = IntegerField("Antennas, cameras, network equipment", [Optional()], render_kw={"placeholder": "0"})
    antennas_destroyed = IntegerField(
        "Antennas, cameras, network equipment Destroyed", [Optional()], render_kw={"placeholder": "0"}
    )
    other = IntegerField("Other", [Optional()], render_kw={"placeholder": "0"})
    other_destroyed = IntegerField("Other Destroyed", [Optional()], render_kw={"placeholder": "0"})
    impact_flights = IntegerField("Impact Flights", [Optional()], render_kw={"placeholder": "0"})
    scouting_flights = IntegerField("Scouting Flights", [Optional()], render_kw={"placeholder": "0"})
    found_targets = IntegerField("Found Targets", [Optional()], render_kw={"placeholder": "0"})
    found_fpv_drones = IntegerField("Found FPV Drones", [Optional()], render_kw={"placeholder": "0"})
    destroyed_fpv_drones = IntegerField("Destroyed FPV Drones", [Optional()], render_kw={"placeholder": "0"})
    mining_flights = IntegerField("Mining Flights", [Optional()], render_kw={"placeholder": "0"})
    setup_mines = IntegerField("Setup Mines", [Optional()], render_kw={"placeholder": "0"})
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
            ("impact_flights", _("Impact Flights")),
            ("scouting_flights", _("Scouting Flights")),
            ("found_targets", _("Found Targets")),
            ("found_fpv_drones", _("Found FPV Drones")),
            ("destroyed_fpv_drones", _("Destroyed FPV Drones")),
            ("mining_flights", _("Mining Flights")),
            ("setup_mines", _("Setup Mines")),
        ],
        validators=[DataRequired()],
    )
    count = IntegerField(_("Count"), [DataRequired()], render_kw={"placeholder": "0"})
    count_destroyed = IntegerField(_("Count Destroyed"), [InputRequired()], default=0)
    submit = SubmitField(_("Save"))
