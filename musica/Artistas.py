from flask import Blueprint, render_template
from.import db

bp = Blueprint('Artistas', __name__, url_prefix='/Artistas')

@bp.route('/')
def generos():
    base_de_datos = db.get_db()
    consulta = """
            SELECT * FROM artists
            ORDER by name;
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("Artistas.html",Artistas=lista_de_resultado)

@bp.route('/<int:id>')
def detalle(id):
    con = db.get_db()
    consulta1 = """
            SELECT * FROM artists
            WHERE ArtistsId = ?;
        """
    consulta2 = """
            SELECT * FROM albums
            WHERE AlbumId = ?;
        """
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_albums = res.fetchall

    pagina = render_template('detalle_artista.html',
                             artista = artista,
                             album = lista_albums)
    return pagina