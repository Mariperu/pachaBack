from flask import Flask

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return f'Numero de Posts {str(len(posts))}'

@app.route("/p/<string:slug>/")
def show_post(slug):
    return f'Mostrando el post {slug}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)