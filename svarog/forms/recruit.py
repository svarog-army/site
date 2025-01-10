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
from svarog import schema as s
from svarog import db


class RecruitForm(FlaskForm):
    next_url = StringField("next_url")
    recruit_uuid = HiddenField("recruit_uuid", [DataRequired()], render_kw={"readonly": True})
    email = StringField("email", [DataRequired(), Email()], render_kw={"placeholder": "Email", "readonly": True})
    full_name = StringField("Full Name", [DataRequired()], render_kw={"placeholder": "Full Name", "readonly": True})
    birth_date = DateField("Birth Date", [DataRequired()], render_kw={"placeholder": "Birth Date", "readonly": True})
    phone = StringField("Phone", [DataRequired()], render_kw={"placeholder": "Phone", "readonly": True})
    city_of_actual_residence = StringField(
        "City of Actual Residence",
        [DataRequired()],
        render_kw={"placeholder": "City of Actual Residence", "readonly": True},
    )
    education = StringField("Education", [DataRequired()], render_kw={"placeholder": "Education", "readonly": True})
    skills = StringField("Skills", [DataRequired()], render_kw={"placeholder": "Skills", "readonly": True})
    last_job = StringField("Last Job", [DataRequired()], render_kw={"placeholder": "Last Job", "readonly": True})
    health_problems = StringField(
        "Health Problems", [DataRequired()], render_kw={"placeholder": "Health Problems", "readonly": True}
    )
    have_driver_license = StringField(
        "Have Driver License", [DataRequired()], render_kw={"placeholder": "Have Driver License", "readonly": True}
    )
    is_serviceman = BooleanField("Is Serviceman", render_kw={"readonly": True})
    uav_experience = TextAreaField(
        "UAV Experience", [DataRequired()], render_kw={"placeholder": "UAV Experience", "readonly": True}
    )
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


class StatusForm(FlaskForm):
    status = SelectField(
        "Status",
        [DataRequired()],
        choices=[
            (s.RecruitStatus.APPLIED.value, "APPLIED"),
            (s.RecruitStatus.IN_PROGRESS.value, "IN PROGRESS"),
            (s.RecruitStatus.REJECTED.value, "REJECTED"),
            (s.RecruitStatus.HIRED.value, "HIRED"),
        ],
        default=None,
        render_kw={"onchange": "this.form.submit()"},
    )


class FilterForm(FlaskForm):
    search = StringField("Search")
    status = SelectField(
        "Status",
        choices=[
            ("", "All"),
            (s.RecruitStatus.APPLIED.value, "APPLIED"),
            (s.RecruitStatus.IN_PROGRESS.value, "IN PROGRESS"),
            (s.RecruitStatus.REJECTED.value, "REJECTED"),
            (s.RecruitStatus.HIRED.value, "HIRED"),
        ],
        default="",
    )
    specialty = SelectField("Specialty", choices=[])

    def __init__(self, specialty_choices=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.specialty.choices = specialty_choices or [("", "All")]
