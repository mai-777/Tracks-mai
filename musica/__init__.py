from flask import Flask, render_template

app = Flask(__name__)

with app.app_context() :
    from . import db
    db.init_app(app)



@app.route('/')
def hello():
    return 'Hello, World!'

from . import Generos
app.register_blueprint(Generos.bp)
from . import Canciones
app.register_blueprint(Canciones.bp)

