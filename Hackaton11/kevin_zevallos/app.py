from flask import Flask, request,render_template,session,redirect,url_for
from flask_orator import Orator, jsonify

# Creating Flask application
app = Flask(__name__)
#app.config.from_object(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
app.config['ORATOR_DATABASES'] = {
    'default': 'postgres',
    'postgres': {
        'driver': 'postgres',
        'host': 'localhost',
        'user': 'postgres',
        'password': 'admin',
        'database': 'minimarket'
    }
}
app.secret_key = 'secret key'
db = Orator(app)
#MODELOS
class Usuario(db.Model):
    __fillable__ = ['user_id','nombre','password','rol']
    __table__ = 'usuarios'
    def compras(self):
        return self.has_many(Venta)
        
class Producto(db.Model):
    __fillable__ = ['product_id','producto','precio_venta','stock']
    __table__ = 'productos'
    def compras(self):
        return self.has_many(Venta)
class Venta(db.Model):
    __fillable__ = ['id_compra','id_usuario','producto','cantidad','monto']
    __table__ = 'ventas'
    def user(self):
        return self.belongs_to(Usuario)

    def product(self):
        return self.belongs_to(Producto)
#RUTAS
@app.route('/')
def index():
    if 'user_id' in session:
        user_id = session['user_id']
        user = Usuario.find(user_id)
        rol=user.to_dict()['rol']
        return render_template('base.html',id = user.id,rol=rol)
    else:
        return redirect(url_for('login'))
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        user = Usuario.where('nombre',nombre).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect("/")  
        

        # En caso de autenticación fallida
        return jsonify({'message': 'Credenciales inválidas'}), 401
    if request.method == 'GET':
        return render_template('login/login.html')

@app.route('/logout')
def logout():
    # Eliminar la información de la sesión
    session.clear()
    # Redireccionar al inicio de sesión u otra página
    return redirect(url_for('login'))    

@app.route('/api/productos/<int:id>',methods=['GET'])
def getRegistros(id):
    usuario = Usuario.find(id)
    if usuario is None:
        return 'El usuario no existe'
    else:
        if request.method == 'GET' and usuario.to_dict()['rol']=='administrador':
            productos=Producto.all()
            return render_template('productos/productos.html',id=usuario.id,productos = productos)
        
        else:
            return 'No tienes permiso para ver los registros :)'
@app.route('/api/productos/update/<int:id>',methods=['GET','POST'])
def updateProduct(id):
    usuario = Usuario.find(id)
    if usuario is None:
        return 'El usuario no existe'
    else:
        if request.method == 'GET' and usuario.to_dict()['rol']=='almacen':
            return render_template('productos/update-product.html',id=usuario.id)
        if request.method == 'POST' and usuario.to_dict()['rol']=='almacen':
            id_producto = request.form['id']
            selected_product = Producto.find(id_producto)
            stock = request.form['stock']
            selected_product.stock = stock
            selected_product.save()
            productos = Producto.all()
            return render_template('productos/productos.html',id = usuario.id,productos = productos)
        else:
            return "no tienes persmisos para actualizar productos :)"
@app.route('/api/productos/update/<int:id>',methods=['GET','POST'])
def createProduct(id):
    usuario = Usuario.find(id)
    if usuario is None:
        return 'El usuario no existe'
    else:
        if request.method == 'GET' and usuario.to_dict()['rol']=='almacen':
            return render_template('productos/create-product.html',id=usuario.id)
        if request.method == 'POST' and usuario.to_dict()['rol']=='almacen':
            producto = request.form['product']
            precio_venta = request.form['precio_venta']
            stock = request.form['stock']
            Producto.create(producto=producto,precio_venta=precio_venta,stock=stock)
            productos=Producto.all()
            return render_template('productos/productos.html',id = usuario.id,productos = productos)
        else:
            return "no tienes persmisos para actualizar productos :)"
@app.route('/api/ventas/<int:id>',methods=['GET'])
def getVentas(id):
    usuario = Usuario.find(id)
    if usuario is None:
        return 'El usuario no existe'
    else:
        if request.method == 'GET' and usuario.to_dict()['rol']=='administrador':
            compras=Venta.all()
            return render_template('ventas/ventas.html',id=usuario.id,compras=compras)
        else:
            return 'No tienes permiso para ver los registros de ventas :)'
@app.route('/api/ventas/create/<int:id>',methods=['POST','GET'])
def createCompra(id):
    usuario = Usuario.find(id)
    if usuario is None:
        return 'El usuario no existe'
    else:
        if request.method == 'GET' and usuario.to_dict()['rol']=='cajero':
            return render_template('ventas/create-venta.html',id=usuario.id)
        if request.method == 'POST' and usuario.to_dict()['rol']=='cajero':
            product_id = request.form['id_producto']
            product = Producto.find(product_id)
            cantidad = request.form['cantidad']
            monto = product.precio_venta * float(cantidad)
            if product is not None and product.stock> 0:
                new_venta=Venta.create(id_usuario=usuario.id,producto = product.producto,cantidad = cantidad,monto = monto)
                cantidad_vendida = new_venta.cantidad
                nuevo_stock = int(product.stock) - int(cantidad_vendida)
                product.stock = str(nuevo_stock)
                product.save()
                return "se creo una nueva venta"
            else:
                return "el producto no se encuentra en la base de datos"
            
            
        else:
            return "no tienes permisos :)"
if __name__ == '__main__':
    app.run(host="localhost",port=8000,debug=True)