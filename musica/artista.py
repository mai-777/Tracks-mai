from flask import Blueprint, render_template, request, redirect, url_for
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
            WHERE a.ArtistId = ?
            AND AlbumId IS NOT NULL
            ORDER by name ASC;
        """
    res = con.execute(consulta1, (id,))
    artista = res.fetchone()
    res = con.execute(consulta2, (id,))
    lista_albums = res.fetchall()

    pagina = render_template('detalle_artista.html',
                             artista = artista,
                             albumes = lista_albums)
    return pagina

@bp.route('/new', methods =('GET', 'POST'))
def nuevo():
   if request.method == 'POST':
       name = request.form['name']
       con = db.get_db()
       consulta = """
               INSERT INTO artists(name)
               VALUES(?)
           """
       con.execute(consulta, (name,))
       con.commit()
       return redirect(url_for('artista.artista'))
   else:
       pagina = render_template('nuevo_artista.html',)
       return pagina