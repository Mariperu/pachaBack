from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, FloatField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    nombre = StringField('Nombre Producto', validators=[DataRequired(), Length(max=128)])
    stock = IntegerField('Stock')
    precio = FloatField('Precio', validators=[DataRequired()],)
    submit = SubmitField('Enviar')
