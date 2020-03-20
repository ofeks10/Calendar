from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CalendarCreateForm(FlaskForm):
    calendar_title = StringField('Calendar Title', validators=[DataRequired()])
    submit = SubmitField('Create')
