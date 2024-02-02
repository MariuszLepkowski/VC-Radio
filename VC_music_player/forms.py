from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


class UrlForm(FlaskForm):
    video_url = StringField("Type YouTube video URL below", validators=[DataRequired(), URL()])
    submit = SubmitField("Go to audio player")
