from flask import request, jsonify, send_file
from app import app, db , cache
from app.token import token_required
from app.model import Movie, Theatre, Booking , UserAuth
from datetime import datetime
from base64 import b64decode, b64encode
from app.mail import send_email
import io

@app.route('/api/create_movie', methods=['POST'])
@token_required
def create_movie():
    data = request.get_json()
    name = data['name']
    description = data['description']
    release_date = data['release_date']
    end_date = data['end_date']
    genre = data['genre']
    language = data['language']
    duration = data['duration']
    price = data['price']
    rating = data['rating']
    cast = data['cast']
    movie_trailer = data['movie_trailer']
    type = data['type']
    theatre_id = data['theatre_id']

    img = b64decode(data['image'])
    
    # img_base64 = b64encode(img).decode()  
    
    if img is None:
        return jsonify({"error": "Image is required"}), 400
    
    theatre = Theatre.query.filter_by(id=theatre_id).first()
    available_seats = theatre.rows * theatre.cols

    movie = Movie(theatre_id=theatre_id, 
                name=name,
                description=description,
                release_date=release_date,
                end_date=end_date,
                genre=genre,
                language=language,
                duration=duration,
                price=price,
                poster=img,
                rating=rating,
                cast=cast,
                movie_trailer=movie_trailer,
                type=type,
                available_seats=available_seats)
    db.session.add(movie)
    db.session.commit()
    #cache
    cache.clear()

    return jsonify({'success': True}), 200


@app.route('/api/update_movie', methods=['GET', 'POST'])
@token_required
def update_movie():
    data = request.get_json()
    movie_id = data['movie_id']
    name = data['name']
    description = data['description']
    release_date = data['release_date']
    end_date = data['end_date']
    genre = data['genre']
    language = data['language']
    duration = data['duration']
    price = data['price']
    rating = data['rating']
    cast = data['cast']
    movie_trailer = data['movie_trailer']
    type = data['type']

    img = b64decode(data['image'])

    movie = Movie.query.filter_by(id=movie_id).first()
    movie.name = name
    movie.description = description
    movie.release_date = release_date
    movie.end_date = end_date
    movie.genre = genre
    movie.language = language
    movie.duration = duration
    movie.price = price
    movie.rating = rating
    movie.cast = cast
    movie.movie_trailer = movie_trailer
    movie.type = type
    movie.poster = img

    #cache
    cache.clear()
    db.session.commit()
    return jsonify({'success': True}), 200


@app.route('/api/delete_movie', methods=['GET', 'POST'])
@token_required
def delete_movie():
    data = request.get_json()
    movie_id = data['movie_id']
    movie = Movie.query.filter_by(id=movie_id).first()
    booking = Booking.query.filter_by(movie_id=movie_id).all()
    if booking:
        db.session.delete(booking)
    db.session.delete(movie)
    db.session.commit()
    
    #cache
    cache.clear()
    return jsonify({'success': True}), 200



@app.route('/api/get_movie_all', methods=['GET', 'POST'])
@token_required
def get_movie_all():
    data = request.get_json()
    admin_id = data['admin_id']

    #cache
    cache_key = f'movie_data_all'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)

    movie = Movie.query.all()
    movie_data = []

    for m in movie:
        movie_data.append({
            'id': m.id,
            'name': m.name,
            'description': m.description,
            'release_date': m.release_date,
            'end_date': m.end_date,
            'genre': m.genre,
            'language': m.language,
            'duration': m.duration,
            'price': m.price,
            'rating': m.rating,
            'cast': m.cast,
            'movie_trailer': m.movie_trailer,
            'type': m.type,
            'available_seats': m.available_seats
        })
    
    #cache
    cache.set(cache_key, movie_data, timeout=5*60)

    return jsonify(movie_data)


@app.route('/api/get_poster_img', methods=['GET', 'POST'])
def get_poster_img():
    data = request.get_json()
    movie_id = data['id']
    #cache

    movie = Movie.query.filter_by(id=movie_id).first()

   
    return send_file(
        io.BytesIO(movie.poster),
        mimetype='image/jpeg'
    )

@app.route('/api/get_movie', methods=['GET', 'POST'])
@token_required
def get_movie():
    data = request.get_json()
    theatre_id = data['theatre_id']

    #cache
    # cache_key = f'movie_data'
    # cached_data = cache.get(cache_key)
    # if cached_data is not None:
    #     return jsonify(cached_data)

    movie = Movie.query.filter_by(theatre_id=theatre_id).all()
    theatre = Theatre.query.filter_by(id=theatre_id).first()
    movie_data = []

    for m in movie:
        movie_data.append({
            'id': m.id,
            'name': m.name,
            'description': m.description,
            'release_date': m.release_date,
            'end_date': m.end_date,
            'genre': m.genre,
            'language': m.language,
            'duration': m.duration,
            'price': m.price,
            'rating': m.rating,
            'cast': m.cast,
            'movie_trailer': m.movie_trailer,
            'type': m.type,
            'available_seats': m.available_seats,
            'theatre_id': theatre.id,
            'theatre_name': theatre.name,
            'theatre_address': theatre.address,
            'theatre_location': theatre.location,
            'theatre_rows': theatre.rows,
            'theatre_cols': theatre.cols,
            'theatre_morning_show_time': theatre.morning_show_time,
            'theatre_matinee_show_time': theatre.matinee_show_time,
            'theatre_first_show_time': theatre.first_show_time,
            'theatre_second_show_time': theatre.second_show_time
        })
    
    
    #cache
    # cache.set(cache_key, movie_data, timeout=5*60)

    return jsonify(movie_data)

@app.route('/api/get_movie_by_id', methods=['GET', 'POST'])
@token_required
def get_movie_by_id():
    data = request.get_json()
    movie_id = data['movie_id']
    #cache
    cache_key = f'movie_data_by_id'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    

    movie = Movie.query.filter_by(id=movie_id).first()
    movie_data = {
        'id': movie.id,
        'name': movie.name,
        'description': movie.description,
        'release_date': movie.release_date,
        'end_date': movie.end_date,
        'genre': movie.genre,
        'language': movie.language,
        'duration': movie.duration,
        'price': movie.price,
        'rating': movie.rating,
        'cast': movie.cast,
        'movie_trailer': movie.movie_trailer,
        'type': movie.type,
        'available_seats': movie.available_seats
    }

    #cache
    cache.set(cache_key, movie_data, timeout=5*60)

    return jsonify(movie_data)




@app.route('/api/get_movie_and_theatre', methods=['GET', 'POST'])
@token_required
def get_movie_and_theatre():
    data = request.get_json()
    
    #cache
    cache_key = f'movie_data_and_theatre'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    

    movie = Movie.query.all()
    movie_data = []
    for m in movie:
        theatre = Theatre.query.filter_by(id=m.theatre_id).first()
        movie_data.append({
            'id': m.id,
            'name': m.name,
            'description': m.description,
            'release_date': m.release_date,
            'end_date': m.end_date,
            'genre': m.genre,
            'language': m.language,
            'duration': m.duration,
            'price': m.price,
            'rating': m.rating,
            'cast': m.cast,
            'movie_trailer': m.movie_trailer,
            'type': m.type,
            'available_seats': m.available_seats,
            'theatre_id': theatre.id,
            'theatre_name': theatre.name,
            'theatre_address': theatre.address,
            'theatre_location': theatre.location,
            'theatre_rows': theatre.rows,
            'theatre_cols': theatre.cols,
            'theatre_morning_show_time': theatre.morning_show_time,
            'theatre_matinee_show_time': theatre.matinee_show_time,
            'theatre_first_show_time': theatre.first_show_time,
            'theatre_second_show_time': theatre.second_show_time
        })
    
    #cache
    cache.set(cache_key, movie_data, timeout=5*60)

    return jsonify(movie_data)






@app.route('/api/get_movie_for_summery', methods=['GET', 'POST'])
@token_required
def get_movie_for_summary():

    #cache
    cache_key = f'movie_data_for_summary'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    
    movie = Movie.query.all()
    movie_data = []
    for m in movie:
        booking = Booking.query.filter_by(movie_id=m.id).all()
        revenue = 0
        booking_dates = []
        booking_times = []
        booking_times_dis = {}
        booking_Unoccupied_seats = {}
        for b in booking:
            revenue = revenue + b.total_price
            if b.movie_date not in booking_dates:
                booking_dates.append(b.movie_date)
            if b.movie_date not in booking_times_dis.keys():
                booking_times_dis[b.movie_date] = [b.movie_time]
            elif b.movie_date in booking_times_dis.keys() and b.movie_time not in booking_times_dis[b.movie_date] :
                booking_times_dis[b.movie_date].append(b.movie_time)
            if b.movie_time not in booking_times:
                booking_times.append(b.movie_time)
            booking_Unoccupied_seats[b.movie_date] = {b.movie_time : m.available_seats - sum([b.seats for b in booking])}
            
        if len(booking) == 0:
            continue
        movie_data.append({
            'id': m.id,
            'name': m.name,
            'admin_rating' : m.rating,
            'user_rating' : sum([b.rating for b in booking])/len(booking),
            'booking_count' : sum([b.seats for b in booking]),
            'Unoccupied_seats' : booking_Unoccupied_seats,
            'date' : booking_dates,
            'time' : booking_times,
            'selectedDate' : '',
            'selectedTime' : '',
            'times' : booking_times_dis,
            'revenue' : revenue
        })

    #cache
    cache.set(cache_key, movie_data, timeout=5*60)
    
    return jsonify(movie_data)

