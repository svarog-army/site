from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class SpecialtyForm(FlaskForm):
    next_url = StringField("next_url")
    specialty_uuid = HiddenField("specialty_uuid", [DataRequired()], render_kw={"readonly": True})
    name_en = StringField("name_en", [DataRequired()], render_kw={"placeholder": "Name (en)"})
    name_uk = StringField("name_uk", [DataRequired()], render_kw={"placeholder": "Name (uk)"})
    is_active = SelectField(
        "Active",
        [DataRequired()],
        choices=[("True", "True"), ("False", "False")],
    )

    submit = SubmitField("Save")


class NewSpecialtyForm(FlaskForm):
    name_en = StringField("name_en", [DataRequired()], render_kw={"placeholder": "Name (en)"})
    name_uk = StringField("name_uk", [DataRequired()], render_kw={"placeholder": "Name (uk)"})
    is_active = SelectField(
        "Active",
        [DataRequired()],
        choices=[("True", "True"), ("False", "False")],
    )

    submit = SubmitField("Save")
