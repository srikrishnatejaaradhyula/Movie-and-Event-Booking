from flask import request, jsonify, render_template
from app import app, db, cache
from app.token import token_required
from datetime import datetime
from app.model import Booking,UserAuth,Movie,Theatre
from app.mail import send_email,send_email_html
from json import dumps,loads

@app.route('/api/create_booking', methods=['POST'])
@token_required
def create_booking():
    data = request.get_json()
    user_id = data['user_id']
    movie_id = data['movie_id']
    seats = data['seats']
    seat_names = dumps(data['seat_names'])
    total_price = data['total_price']
    movie_date = data['movie_date']
    movie_time = data['movie_time']
    booking_time = datetime.now()
    rating = 0

    booking = Booking(user_id=user_id,movie_id=movie_id,seats=seats,seat_names=seat_names,total_price=total_price,movie_date=movie_date,movie_time=movie_time,booking_time=booking_time,rating=rating)

    db.session.add(booking)
    movie = Movie.query.filter_by(id=movie_id).first()
    user = UserAuth.query.filter_by(id=user_id).first()
    body = render_template("movie_ticket.html",seats=seat_names, price=total_price, user_id=user_id,time=booking_time,date=movie_date,movie_title=movie.name,user_name=user.name)

    send_email_html("mad2project.ticketshow@gmail.com",user.email, 'Booking Confirmation', body)
    db.session.commit()

    #cache
    cache.clear()
    
    return jsonify({'success': True}), 200

@app.route('/api/get_user_booking', methods=['GET', 'POST'])
@token_required
def get_user_booking():

    #cache
    cache_key = 'booking_data'
    booking_data = cache.get(cache_key)
    if booking_data:
        return jsonify(booking_data)
    

    data = request.get_json()
    user_id = data['user_id']
    booking = Booking.query.filter_by(user_id=user_id).all()
    booking_data = []
    for b in booking:
        movie = Movie.query.filter_by(id=b.movie_id).first()
        theatre = Theatre.query.filter_by(id=movie.theatre_id).first()
        booking_data.append({
            'id': b.id,
            'movie_name': movie.name,
            'theatre_name': theatre.name,
            'type': movie.type,
            'language': movie.language,
            'seats': b.seats,
            'seats_booked': loads(b.seat_names),
            'total_price': b.total_price,
            'booking_time': b.booking_time,
            'movie_date': b.movie_date,
            'movie_time': b.movie_time,
            'rating': b.rating
        })
    #cache
    cache.set(cache_key, booking_data, timeout=5 * 60)
    return jsonify(booking_data) 

@app.route('/api/get_booking_by_movie', methods=['GET', 'POST'])
@token_required
def get_booking_by_movie():
    data = request.get_json()
    movie_id = data['movie_id']
    movie_date = data['date']
    movie_time = data['time']
    booking = Booking.query.filter_by(movie_id=movie_id,movie_date=movie_date,movie_time=movie_time).all()
    movie = Movie.query.filter_by(id=movie_id).first()
    theatre = Theatre.query.filter_by(id=movie.theatre_id).first()
    
    booked_seats = []
    if booking:
        for b in booking:
            booked_seats+=loads(b.seat_names)

    booking_data = {
        'price': movie.price,
        'rows': theatre.rows,
        'cols': theatre.cols,
        'booked_seats': booked_seats,
    }

    return jsonify(booking_data)


@app.route('/api/update_rating', methods=['GET', 'POST'])
@token_required
def update_rating():
    data = request.get_json()
    booking_id = data['booking_id']
    rating = data['rating']
    booking = Booking.query.filter_by(id=booking_id).first()
    booking.rating = rating
    #cache
    # cache.delete('booking_data')
    # cache.delete('booking_data_by_id')

    cache.clear()

    db.session.commit()
    return jsonify({'success': True}), 200

@app.route('/test_mail', methods=['GET', 'POST'])
def test_mail():
    movie_title = "sample movie"
    user_name = "sample user"
    seats = ["A1","A2","A3"]
    time_date = "date time"
    price = "price"
    body = render_template("movie_ticket.html",movie_title=movie_title,user_name=user_name,seats=seats,time_date=time_date,price=price)
    send_email_html("mad2project.ticketshow@gmail.com","srikrishnateja2002@gmail.com", 'Booking Confirmation Test', body)
    return jsonify({'success': True}), 200





