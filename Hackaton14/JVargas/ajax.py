
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/realizar_venta', methods=['POST'])
def realizar_venta():
    return jsonify({'message': 'Venta realizada correctamente'})

if __name__ == '__main__':
    app.run()
