from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    nombre='prueba1'
    return '''
        
<html>
<body>
hola %s
<img src="static/kawa2.png">
</body>
</html>
''' % nombre


