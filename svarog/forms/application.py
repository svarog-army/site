from flask_wtf import FlaskForm
from wtforms import DateField, EmailField, RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Email
from wtforms_sqlalchemy.fields import QuerySelectMultipleField

from svarog import db
from svarog import models as m


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
    is_serviceman = RadioField("Is Serviceman", choices=[("yes", "Так"), ("no", "Ні")], validators=[DataRequired()])
    uav_experience = StringField("UAV Experience", [DataRequired()])
    applied_specialties = QuerySelectMultipleField(
        "Applied Specialties",
        query_factory=lambda: db.session.query(m.Specialty),
        get_pk=lambda x: x.id,
        get_label=lambda x: x.name,
        allow_blank=False,
    )
    submit = SubmitField("Save")
