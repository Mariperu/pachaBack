from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FloatField, validators
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    nombre = StringField("Nombre de producto", validators=[DataRequired(), Length(max=50)])
    categoria = StringField("Categoria", validators=[DataRequired(), Length(max=25)])
    stock = IntegerField("Stock", validators=[DataRequired()])
    precioUnitario = FloatField("Precio Unitario", validators=[DataRequired()])
    submit = SubmitField("Enviar")