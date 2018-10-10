from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    nombre='pp'
    return 'Página principal'

@app.route('/hola')
def index():
    return 'hola'




