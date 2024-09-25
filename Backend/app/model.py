from app import db


class UserAuth(db.Model):
    __tablename__ = 'userauth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    verified = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(80), nullable=False)

 
class AdminAuth(db.Model):
    __tablename__ = 'adminauth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    last_login = db.Column(db.DateTime)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)


class Theatre(db.Model):
    __tablename__ = 'theatre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    rows = db.Column(db.Integer, nullable=False)
    cols = db.Column(db.Integer, nullable=False)
    morning_show_time = db.Column(db.String(100))
    matinee_show_time = db.Column(db.String(100))
    first_show_time = db.Column(db.String(100))
    second_show_time = db.Column(db.String(100))
    admin_id = db.Column(db.Integer, db.ForeignKey('adminauth.id' , onupdate='CASCADE', ondelete='CASCADE'), nullable=False)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    poster = db.Column(db.LargeBinary)
    genre = db.Column(db.String(120), nullable=False)
    release_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=False)
    cast = db.Column(db.String(500), nullable=False)
    language = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.String(120), nullable=False)
    movie_trailer = db.Column(db.String(500), nullable=False)
    type = db.Column(db.String(120), nullable=False) # 2D, 3D, 4D
    price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seat_names = db.Column(db.String(500), nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    movie_date = db.Column(db.String(50), nullable=False)
    movie_time = db.Column(db.String(50), nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('userauth.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    

class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brochure = db.Column(db.LargeBinary)
    form = db.Column(db.String(1000), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('adminauth.id' , onupdate='CASCADE', ondelete='CASCADE'), nullable=False)

class EventBooking(db.Model):
    __tablename__ = 'eventbooking'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    form = db.Column(db.String(1000), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('userauth.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    