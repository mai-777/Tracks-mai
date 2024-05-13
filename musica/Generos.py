from flask import Blueprint, render_template
from.import db

bp = Blueprint('genero', __name__, url_prefix='/genero')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
            SELECT name FROM genres
            ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("genero.html",generos=lista_de_resultado)

@bp.route('/<init:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
            SELECT name FROM genres
            WHERE GenreId = ?;
        """
    consulta2 = """
            SELECT t.name,g.name as genero FROM tracks t
            JOIN albums a ON t.TrackId = a.AlbumId
            JOIN artists s ON a.AlbumId = s.ArtistId
            JOIN genres g ON s.ArtistId = GenreId
            ORDER BY g.name ASC
        """
    res = con.execute(consulta1, (id,))
    genero = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_canciones = res.fetchall

    pagina = render_template('detalle_genero.html',
                             genero = genero,
                             canciones = lista_canciones)
    return pagina








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
