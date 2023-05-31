from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, TextAreaField,DateField,validators
from wtforms.validators import DataRequired, Length


class RolForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Enviar')