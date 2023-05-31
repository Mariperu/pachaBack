from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    nombre = StringField('Nombre Producto', validators=[DataRequired(), Length(max=30)])
    stock = IntegerField('Stock', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class UserAdminForm(FlaskForm):
    rol = StringField('Rol')
    submit = SubmitField('Guardar')