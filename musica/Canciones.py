
@app.route('/track')
def tracks():
    base_de_datos = db.get_db()
    consulta = """
            SELECT t.name,s.name as artistas FROM tracks t
            JOIN albums a ON t.TrackId = a.AlbumId
            JOIN artists s ON a.AlbumId = s.ArtistId
            ORDER BY t.name ASC
    """
    resultado = base_de_datos.execute(consulta)
    lista_de_resultado = resultado.fetchall()
    return render_template("track.html",tracks=lista_de_resultado)