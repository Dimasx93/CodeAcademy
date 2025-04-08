from flask_wtf import FlaskForm
from wtforms.fields.datetime import DateField
from wtforms.fields.simple import TextAreaField, SubmitField
from wtforms.validators import DataRequired
from wtforms import StringField, validators


class TaskForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    description = TextAreaField("Description")
    due_date = DateField("Due Date", validators=(validators.Optional(),))
    submit = SubmitField("Add Task")