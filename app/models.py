from app import app
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import VARCHAR
from sqlalchemy.orm import Mapped


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
        "artists", backref=db.backref("artists.ArtistId", uselist=True)
    )


@dataclass
class customers(db.Model):
    __tablename__ = "customers"
    CustomerId: int
    CustomerId = db.Column(db.Integer, primary_key=True)
    FirstName: str
    FirstName = db.Column(VARCHAR)
    LastName: str
    LastName = db.Column(VARCHAR)
    Company: str
    Company = db.Column(VARCHAR)
    City: str
    City = db.Column(VARCHAR)
    State: str
    State = db.Column(VARCHAR)
    Country: str
    Country = db.Column(VARCHAR)
    PostalCode: str
    PostalCode = db.Column(VARCHAR)
    Phone: str
    Phone = db.Column(VARCHAR)
    Fax: str
    Fax = db.Column(VARCHAR)
    Email: str
    Email = db.Column(VARCHAR)
    SupportRepId: int
    SupportRepId = db.Column(db.Integer, db.ForeignKey("employees.EmployeeId"))
    supportrepid = db.relationship(
        "employees", backref=db.backref("employees.EmployeeId")
    )


@dataclass
class employees(db.Model):
    EmployeeId: int = db.Column(db.Integer, primary_key=True)
    FirstName: str = db.Column(VARCHAR)
    LastName: str = db.Column(VARCHAR)
    Title: str = db.Column(VARCHAR)
    ReportsTo: str
    ReportsTo = db.Column(db.Integer, db.ForeignKey("employees.EmployeeId"))

    SuperVisor: Mapped[list["SuperVisor"]] = db.relationship(
        "employees",
        backref=db.backref("employees.ReportsTo"),
        remote_side="employees.EmployeeId",
    )


###################################################################################
# Old style sqlalchemy queries vs new style 2.0.x queries

# User.query.all() #old
# db.session.execute(db.select(User)).scalars().all() # new
# db.session.scalars(db.select(User)).all() # new with shortcut

# User.query.first()
# db.session.scalars(db.select(User)).first()

# User.query.filter_by(name="Anthony").first()
# db.session.scalars(db.select(User).filter_by(name="Anthony")).first()

# User.query.filter(User.name != "Anthony").all()
# db.session.scalars(db.select(User).where(User.name != "Anthony")).all()

# User.query.get(4)
# db.session.get(User, 4)

# User.query.count()
# db.session.scalar(db.func.count(User.id))
###################################################################################
