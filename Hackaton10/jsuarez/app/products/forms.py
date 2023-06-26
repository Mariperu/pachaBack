from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,DateField,validators
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    producto = StringField('producto', validators=[DataRequired(), Length(max=128)])
    stock = StringField('stock', validators=[DataRequired(), Length(max=128)])
    precio = StringField('precio', validators=[DataRequired(), Length(max=128)])
    submit = SubmitField('Enviar')