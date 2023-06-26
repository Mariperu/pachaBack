from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,DateField,validators
from wtforms.validators import DataRequired, Length


class PerfilForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    apellido = StringField('Apellido', validators=[DataRequired(), Length(max=128)])
    pais = StringField('Pais', validators=[DataRequired(), Length(max=128)])
    ciudad = StringField('Ciudad', validators=[DataRequired(), Length(max=128)])
    fechaNacimiento = DateField('Fecha Nacimiento', format='%m/%d/%Y', validators=(validators.Optional(),))
    info = TextAreaField('Contenido')
    avatar = StringField('Avatar')
    url = StringField('URL')
    facebook = StringField('Facebook')
    twitter=StringField('Twitter')
    submit = SubmitField('Enviar')