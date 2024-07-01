from flask import Blueprint, render_template
from.import db

bp = Blueprint('artista', __name__, url_prefix='/artista')

@bp.route('/')
def artista():
    base_de_datos = db.get_db()
    consulta = """
            SELECT name, ArtistId FROM artists
            ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("artista.html",artista=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
            SELECT name, ArtistId FROM artists
            WHERE ArtistId = ?;
        """
    consulta2 = """
            SELECT a.ArtistId, name, b.Title as titulo, b.AlbumId FROM artists a 
            LEFT JOIN albums b ON a.ArtistId = b.ArtistId
            WHERE AlbumId = ?
            AND AlbumId IS NOT NULL
            ORDER by name ASC;
        """
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_albums = res.fetchall

    pagina = render_template('detalle_artista.html',
                             artista = artista,
                             album = lista_albums)
    return pagina