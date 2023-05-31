from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, IntegerField, FloatField, validators
from wtforms.validators import DataRequired, Length

class VentaForm(FlaskForm):
    fechaVenta = DateField("Fecha Venta", validators=[DataRequired()])
    nombre = StringField("Nombre de producto", validators=[DataRequired(), Length(max=50)])
    categoria = StringField("Categoria", validators=[DataRequired(), Length(max=25)])
    stock = IntegerField("Stock", validators=[DataRequired()])
    precioUnitario = FloatField("Precio Unitario", validators=[DataRequired()])
    subTotal = FloatField("SubTotal", validators=[DataRequired()])
    submit = SubmitField("Enviar")