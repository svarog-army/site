from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CustomLinksForm(FlaskForm):
    instagram_url = StringField("Instagram", render_kw={"placeholder": "Instagram URL"})
    facebook_url = StringField("Facebook", render_kw={"placeholder": "Facebook URL"})
    telegram_url = StringField("Telegram", render_kw={"placeholder": "Telegram URL"})
    youtube_url = StringField("YouTube", render_kw={"placeholder": "YouTube URL"})
    donate_url = StringField("Donate", render_kw={"placeholder": "Donate URL"})
    test_drive_url = StringField("Test Drive", render_kw={"placeholder": "Test Drive URL"})
    coffee_box_url = StringField("Coffee Box", render_kw={"placeholder": "Coffee Box URL"})
    submit = SubmitField("Save")
