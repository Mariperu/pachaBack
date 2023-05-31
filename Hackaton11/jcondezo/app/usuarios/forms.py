from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length
from app.models import Cliente

class ClienteForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    dni = StringField('Dni', validators=[DataRequired()])
    celular = StringField('Celular')
    direccion = StringField('Dirección')
    submit = SubmitField('Enviar')
