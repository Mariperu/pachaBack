from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length
from app.models import Rol

class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    # role_id = IntegerField('Rol', validators=[DataRequired()])
    role_id = SelectField('Categoria', coerce=int)
    submit = SubmitField('Registrar')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.role_id.choices = [(interval.id, interval.nombre)
                                        for interval in Rol.query.all()]


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Login')