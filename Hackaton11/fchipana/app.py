from flask import Flask, request, jsonify
from flask_orator import Orator
from models import Cliente_table, Producto_table, Venta_table, DetalleVenta_table
from config import ORATOR_DATABASES

app = Flask(__name__)
app.config['ORATOR_DATABASES'] = ORATOR_DATABASES

db = Orator(app)

@app.get('/')
def home():
    # response = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
    return 'running...'

@app.post('/api/crearCliente')
def crearCliente():
    data = request.get_json()
    Cliente_table.create(**data)
    return 'cliente creado correctamente'

@app.post('/api/crearProducto')
def crearProducto():
    data = request.get_json()
    Producto_table.create(**data)
    return 'producto creado correctamente'

@app.post('/api/crearVenta')
def crearVenta():
    data = request.get_json()
    # buscar al cliente
    client = Cliente_table.where('nombre', data['cliente']['nombre']).first()
    print('client', client)
    if client:
        print('client', client)
        # Crear instancia de Venta_table y asociar cliente
        venta = Venta_table.create(fecha_venta=data['fecha'], monto_total=data['total'], id_cliente=client.to_dict()['id_cliente'])

        # Crear instancias de DetalleVenta_table y asociar productos
        for producto_data in data['productos']:
            producto = Producto_table.where('nombre', producto_data['nombre']).first()

            if producto:
                DetalleVenta_table.create(cantidad=producto_data['cantidad'], subtotal=producto.to_dict()['precio'], id_venta=venta.to_dict()['id_venta'], id_producto=producto.to_dict()['id_producto'])

        return 'Venta creada correctamente'
    else:
        return 'Cliente no encontrado'

@app.route('/api/ventas', methods=['GET'])
def listar_ventas():
    ventas = Venta_table.with_('cliente', 'detalle_ventas.producto').get()
    resultado = []

    for venta in ventas:
        productos = []
        for detalle_venta in venta.detalle_ventas:
            productos.append({
                'id_producto': detalle_venta.producto.id_producto,
                'nombre_producto': detalle_venta.producto.nombre,
                'cantidad': detalle_venta.cantidad,
                'subtotal': detalle_venta.subtotal
            })

        resultado.append({
            'id_venta': venta.id_venta,
            'fecha_venta': venta.fecha_venta,
            'nombre_cliente': venta.cliente.nombre,
            'productos': productos
        })

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)