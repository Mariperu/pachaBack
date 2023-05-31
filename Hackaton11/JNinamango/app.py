from flask import Flask, redirect, render_template, request, url_for
from flask_orator import Orator
from flask_sqlalchemy import SQLAlchemy

ORATOR_DATABASES = {
    'default': 'minimarket',
    'minimarket':{
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'warstrategoC123',
        'database': 'minimarket'
    }
}
app = Flask(__name__)
app.config.from_object(__name__)  # Carga la configuración desde el archivo config.py
db = Orator(app)
precio = 0.0
class UserTable(db.Model):
    __fillable__ = ['name', 'username', 'password', 'roles']
    class Meta:
        table = 'user_table'

class ProductTable(db.Model):
    __fillable__ = ['nombre', 'precio', 'stock']
    class Meta:
        table = 'productos'




@app.route('/', methods = ['POST', 'GET'])
def index():
    print(ProductTable.all()[0].nombre)
    return render_template('base.html')


@app.route("/users/login", methods = ['POST', 'GET'])
def checkLogin():

    if(request.method == 'POST'):
        user = UserTable.where('username', request.form["username"]).first()
        if(user is None):
            return "registrate, retrocede..."
        else:
            if(user.roles == 'Almacen'):
                return render_template('preupdate_products.html', listaProducts = ProductTable.all())
            elif(user.roles == 'Admin'):
                return render_template('ver_products.html', listaProducts = ProductTable.all())
            else:
                return render_template('comprarProducts.html')
                
    else:
        return render_template("login.html")

@app.route("/almacen/updateProducto/", methods=['POST', 'GET'])
def update_producto_form():
    id = request.form["id"]
    prod = ProductTable.find(id)
    return render_template('update_products.html', producto = prod)




@app.route("/almacen/comprarProducts/", methods=['POST', 'GET'])
def comprar_producto_form():
    global precio
    precio = precio + float(request.form["precio"])
    return render_template('comprarProducts.html', precio = precio)


@app.route('/users/create', methods=['POST', 'GET'] )
def create_user_form():

    if request.method == 'POST': 
        name_ = request.form['name']
        username_ = request.form['username']
        password_ = request.form['password']
        rol_ = request.form['rol']

        UserTable.create(name=name_, username=username_, password=password_, roles=rol_)
        return "ahora si, logeate y tendras acceso a tus funciones"
    else:
        roles = ['Admin', 'Cajero', 'Almacen']
        return render_template('create_user.html', roles=roles)

if __name__ == '__main__':
    
    app.run(debug=True)