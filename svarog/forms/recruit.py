from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    ValidationError,
    HiddenField,
    DateField,
    BooleanField,
    TextAreaField,
    SelectField,
)
from wtforms.validators import DataRequired, Email

from svarog import models as m
from svarog import db


class RecruitForm(FlaskForm):
    next_url = StringField("next_url")
    recruit_uuid = HiddenField("recruit_uuid", [DataRequired()], render_kw={"readonly": True})
    email = StringField("email", [DataRequired(), Email()], render_kw={"placeholder": "Email"})
    full_name = StringField("Full Name", [DataRequired()], render_kw={"placeholder": "Full Name"})
    birth_date = DateField("Birth Date", [DataRequired()], render_kw={"placeholder": "Birth Date"})
    phone = StringField("Phone", [DataRequired()], render_kw={"placeholder": "Phone"})
    city_of_actual_residence = StringField(
        "City of Actual Residence", [DataRequired()], render_kw={"placeholder": "City of Actual Residence"}
    )
    education = StringField("Education", [DataRequired()], render_kw={"placeholder": "Education"})
    skills = StringField("Skills", [DataRequired()], render_kw={"placeholder": "Skills"})
    last_job = StringField("Last Job", [DataRequired()], render_kw={"placeholder": "Last Job"})
    health_problems = StringField("Health Problems", [DataRequired()], render_kw={"placeholder": "Health Problems"})
    have_driver_license = StringField(
        "Have Driver License", [DataRequired()], render_kw={"placeholder": "Have Driver License"}
    )
    is_serviceman = BooleanField("Is Serviceman")
    uav_experience = TextAreaField("UAV Experience", [DataRequired()], render_kw={"placeholder": "UAV Experience"})
    status = SelectField(
        "Status",
        [DataRequired()],
        choices=[("APPLIED", "APPLIED"), ("IN_PROGRESS", "IN_PROGRESS"), ("REJECTED", "REJECTED"), ("HIRED", "HIRED")],
    )
    comments = TextAreaField("Comments")

    submit = SubmitField("Save")

    def validate_full_name(self, field):
        query = (
            m.Recruit.select().where(m.Recruit.full_name == field.data).where(m.Recruit.uuid != self.recruit_uuid.data)
        )
        if db.session.scalar(query) is not None:
            raise ValidationError("This recruit name is already in use.")

    def validate_email(self, field):
        query = m.Recruit.select().where(m.Recruit.email == field.data).where(m.Recruit.uuid != self.recruit_uuid.data)
        if db.session.scalar(query) is not None:
            raise ValidationError("This email is already registered.")
