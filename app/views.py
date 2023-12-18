from app import app
from flask import request, render_template, abort, jsonify, abort
from sqlalchemy.sql.operators import ilike_op, like_op
from sqlalchemy import text
from app.models import db, artists, albums, employees, customers


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


@app.route("/album/<num>")
def album(num):
    """uses new style sqlalchemy query"""
    num = int(num)
    album_num = db.session.scalars(db.select(albums).where(albums.AlbumId == num)).one()
    if album_num:
        return jsonify(album_num)
    else:
        abort(404)


@app.route("/artist/<name>")
def artist(name):
    "uses new style sqlalchemy queries to perform a 'ilike' type query"
    artist_name = db.session.scalars(
        db.select(albums).filter(ilike_op(artists.Name, f"%{name}%"))
    ).all()

    return jsonify(artist_name)


@app.route("/match/<name>")
def match(name):
    """example query using new style that demonstrates a where and ilike query combined"""
    artist_to_albums = db.session.scalars(
        db.Query(albums)
        .join(artists, isouter=False)
       
        .filter(artists.ArtistId == albums.ArtistId)
        .where(
             ilike_op(artists.Name, f"%{name}%")
        )
    ).all()
    print(artist_to_albums)
    return jsonify(artist_to_albums)


@app.route("/employees/<directs>")
def employeedata(directs):
    data = employees.query.all()
    # db.session.scalars(db.select(User).where(User.name != "Anthony")).all()
    #db.session.scalars(db.select(User).filter_by(name="Anthony")).first()
    filter_data = db.session.scalars(db.select(employees).filter_by(ReportsTo=directs)).all()
    print(filter_data)
    return render_template("employees.html", data=data, directs=directs ,filter_data=filter_data)


@app.route("/customers/<id>", methods=["GET", "POST"])
def customer(id) -> str:
    """get the customer by ID and display the support rep for that customer"""
    try:
        data = customers.query.filter_by(CustomerId=id).all()
        support_rep = employees.query.filter_by(EmployeeId=data[0].SupportRepId).one()
        print(support_rep)
    except IndexError as ie:
        return f"{abort(404)} : {ie}"
    else:
        return render_template("customers.html", data=data, support_rep=support_rep)
