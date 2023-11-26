from app import app
from flask import request, render_template, abort, jsonify, abort
from app.models import db, artists, albums


@app.route("/test")
def main_route():
    return "<h1> you are at main route</h1>"


@app.route("/art")
def name():
    """testing out both old and new sqlalchemy queries"""
    num = request.args.get("num")
    num = int(num)
    # data = db.session.scalars(db.select(albums, artists).where(albums.AlbumId == num and(albums.ArtistId == artists.ArtistId ))).all()
    try:
        data = artists.query.filter(artists.ArtistId == num).all()

        album = albums.query.filter(albums.ArtistId == data[0].ArtistId).all()
        all_data = {"artist": data, "album": album}
        return jsonify(all_data)
    except IndexError as ie:
        return f"{abort(404)} : {ie}"
