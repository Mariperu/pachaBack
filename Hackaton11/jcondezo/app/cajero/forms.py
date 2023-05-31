from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, DateField, validators, SelectField
from wtforms.validators import DataRequired, Length
from app.models import Producto, Cliente

class FacturaForm(FlaskForm):
    fecha = DateField('Fecha', validators=[DataRequired()])
    cliente_id = SelectField('Cliente', coerce=int)
    producto_id = SelectField('Producto', coerce=int)
    Cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    MontoTotal = FloatField('Monto a Pagar', validators=[DataRequired()])
    submit = SubmitField('Enviar')


    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        self.producto_id.choices = [(interval.id, interval.nombre)
                                        for interval in Producto.query.all()]

        self.cliente_id.choices = [(cli.id, cli.dni)
                                        for cli in Cliente.query.all()]