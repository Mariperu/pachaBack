from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField, FloatField, FormField, FieldList, Form
from wtforms.validators import DataRequired, Length


class DetalleFacturaForm(Form):
    nombre = StringField('Nombre Producto', validators=[DataRequired(), Length(max=128)])
    precio = FloatField('Precio', validators=[DataRequired()], )
    cantProducto = IntegerField('cantProducto')


class FacturaForm(FlaskForm):
    numero_factura = StringField('Número de Factura', validators=[DataRequired()])
    cliente = StringField('Cliente', validators=[DataRequired()])
    detalles = FieldList(FormField(DetalleFacturaForm), min_entries=1)
    submit = SubmitField('Crear Factura')