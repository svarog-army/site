from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, HiddenField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from svarog import models as m
from svarog import db


class UserForm(FlaskForm):
    next_url = StringField("next_url")
    user_uuid = HiddenField("user_uuid", [DataRequired()], render_kw={"readonly": True})
    email = StringField("email", [DataRequired(), Email()], render_kw={"placeholder": "Email"})
    is_admin = BooleanField("Is Admin")
    username = StringField("Username", [DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField("Password", render_kw={"placeholder": "Password"})
    password_confirmation = PasswordField(
        "Confirm Password",
        validators=[
            EqualTo("password", message="Password do not match."),
        ],
        render_kw={"placeholder": "Confirm Password"},
    )
    submit = SubmitField("Save")

    def validate_username(self, field):
        query = m.User.select().where(m.User.username == field.data).where(m.User.uuid != self.user_uuid.data)
        if db.session.scalar(query) is not None:
            raise ValidationError("This username is taken.")

    def validate_email(self, field):
        query = m.User.select().where(m.User.email == field.data).where(m.User.uuid != self.user_uuid.data)
        if db.session.scalar(query) is not None:
            raise ValidationError("This email is already registered.")

    def validate_password(self, field):
        if field.data and len(field.data) <= 6:
            raise ValidationError("Password length must be more than 6 symbols .")


class NewUserForm(FlaskForm):
    email = StringField("email", [DataRequired(), Email()], render_kw={"placeholder": "Email"})
    is_admin = BooleanField("Is Admin")
    username = StringField("Username", [DataRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(6, 30)], render_kw={"placeholder": "Password"}
    )
    password_confirmation = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Password do not match."),
        ],
        render_kw={"placeholder": "Confirm Password"},
    )
    submit = SubmitField("Save")

    def validate_username(self, field):
        query = m.User.select().where(m.User.username == field.data)
        if db.session.scalar(query) is not None:
            raise ValidationError("This username is taken.")

    def validate_email(self, field):
        query = m.User.select().where(m.User.email == field.data)
        if db.session.scalar(query) is not None:
            raise ValidationError("This email is already registered.")
