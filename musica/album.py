from flask import Blueprint, render_template
from.import db

bp = Blueprint('album', __name__, url_prefix='/album')

@bp.route('/')
def album():
    base_de_datos = db.get_db()
    consulta = """
            SELECT Title, AlbumId FROM albums
            ORDER by Title;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("album.html",album=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
            SELECT Title, AlbumId FROM albums
            WHERE AlbumId = ?;
        """
    consulta2 = """
            SELECT t.name, t.TrackId FROM tracks t
            WHERE AlbumId = ?;
        """
    res = con.execute(consulta1, (id,))
    album = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_canciones = res.fetchall

    pagina = render_template('detalle_album.html',
                             album = album,
                             cancion = lista_canciones)
    return pagina