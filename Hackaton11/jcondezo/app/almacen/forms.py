from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from app.models import Categoria


class CategoriaForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    descripcion = StringField('Descripcion')
    submit = SubmitField('Enviar')


class ProductoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired(), Length(max=128)])
    descripcion = StringField('Descripcion')
    cantidad = IntegerField('Cantidad', validators=[DataRequired()])
    marca = StringField('Marca', validators=[DataRequired()])
    precio = FloatField('Precio', validators=[DataRequired()])
    categoria_id = SelectField('Categoria', coerce=int)
    submit = SubmitField('Enviar')

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.categoria_id.choices = [(interval.id, interval.nombre)
                                        for interval in Categoria.query.all()]
