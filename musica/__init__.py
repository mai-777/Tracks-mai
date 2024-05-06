from flask import Flask, render_template

app = Flask(__name__)

with app.app_context() :
    from . import db
    db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/genero')
def generos():
    base_de_datos = db.get_db()
    consulta = """
            SELECT name FROM genres
            ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero.html",generos=lista_de_resultado)

@app.route('/album')
def albums():
    base_de_datos = db.get_db()
    consulta = """
            SELECT Title FROM albums
            ORDER by Title;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("album.html",albums=lista_de_resultado)

@app.route('/track')
def tracks():
    base_de_datos = db.get_db()
    consulta = """
            SELECT name FROM tracks
            ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("track.html",tracks=lista_de_resultado)