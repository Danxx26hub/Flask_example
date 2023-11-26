from app import app
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)


@dataclass
class artists(db.Model):
    __tablename__ = "artists"
    ArtistId: int
    Name: str
    ArtistId = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(300))


@dataclass
class albums(db.Model):
    __tablename__ = "albums"
    AlbumId: int
    Title: str
    ArtistId: int
    AlbumId = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(300))
    ArtistId = db.Column(db.Integer, db.ForeignKey("artists.ArtistId"))
    artistsid = db.relationship(
        "artists", backref=db.backref("artists.ArtistId", uselist=False)
    )
