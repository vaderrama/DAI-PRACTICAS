from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    nombre='prueba2'
    return '''
        
<html>
<body>
hola %s
<img src="static/kawa.png">
</body>
</html>
''' % nombre


