from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    identificador = StringField('Identificador', validators=[Length(max=128)])
    edad = IntegerField('Edad')
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')

class ProfesorForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    identificador = StringField('Identificador', validators=[Length(max=128)])
    edad = IntegerField('Edad')
    correo = StringField('Correo', validators=[DataRequired(), Email()])
    submit = SubmitField('Enviar')

class CursoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    identificador = StringField('Identificador', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Enviar')

class SalonForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    anioEscolar = IntegerField('AnioEscolar')
    submit = SubmitField('Enviar')