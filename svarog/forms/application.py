import re
from flask import g
from flask_wtf import FlaskForm
from wtforms import DateField, EmailField, RadioField, StringField, SubmitField, widgets, ValidationError
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectMultipleField
from flask_babel import _

from svarog import db
from svarog import models as m
from svarog.utils import YesOrNo


class SpecialtyField(QuerySelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


def get_specialty_label(specialty: m.Specialty) -> str:
    if g.lang_code == "uk":
        return specialty.name_uk
    return specialty.name


def get_yes_or_no_choices() -> list[tuple[str, str]]:
    return [
        (YesOrNo.YES.value, _("Yes")),
        (YesOrNo.NO.value, _("No")),
    ]


class ApplicationForm(FlaskForm):
    full_name = StringField(
        "Full Name",
        [DataRequired()],
    )
    birth_date = DateField("Birth Date", [DataRequired()])
    phone = StringField("Phone", [DataRequired()])
    email = EmailField("Email", [DataRequired(), Email()])
    city_of_actual_residence = StringField("City of Actual Residence", [DataRequired()])
    education = StringField("Education", [DataRequired()])
    skills = StringField("Skills", [DataRequired()])

    last_job = StringField("Last Job", [DataRequired()])
    health_problems = StringField("Health Problems", [DataRequired()])
    have_driver_license = StringField("Have Driver License", [DataRequired()])
    is_serviceman = RadioField(
        "Is Serviceman",
        choices=get_yes_or_no_choices,  # we use lambda here to make in-place translation
        validators=[DataRequired()],
    )
    uav_experience = StringField("UAV Experience", [DataRequired()])
    allow_data_processing = RadioField(
        "Is Serviceman",
        choices=get_yes_or_no_choices,
        validators=[DataRequired()],
    )
    applied_specialties = SpecialtyField(
        "Applied Specialties",
        query_factory=lambda: db.session.query(m.Specialty).where(m.Specialty.is_deleted.is_(False)),
        get_pk=lambda x: x.id,
        get_label=get_specialty_label,
        allow_blank=False,
    )
    submit = SubmitField("Save")

    def validate_phone(form, field):
        if not re.match(r"^\+380 \(\d{2}\) \d{3}-\d{2}-\d{2}$", field.data):
            raise ValidationError("Please enter a valid Ukrainian phone number in the format: +380 (XX) XXX-XX-XX")
