from flask import request, jsonify
from app import app, db, cache, logging
from app.token import token_required
from app.model import Theatre,Booking,Movie

@app.route('/api/create_theatre', methods=['POST'])
@token_required
def create_post():
    data = request.get_json()
    name = data['name']
    address = data['address']
    location = data['location']
    rows = data['rows']
    cols = data['cols']
    morning_show_time = data['morning_show_time']
    matinee_show_time = data['matinee_show_time']
    first_show_time = data['first_show_time']
    second_show_time = data['second_show_time']
    admin_id = data['admin_id']

    theatre = Theatre(admin_id=admin_id, name=name, address=address, location=location, rows=rows, cols=cols, morning_show_time=morning_show_time, matinee_show_time=matinee_show_time, first_show_time=first_show_time, second_show_time=second_show_time)
    db.session.add(theatre)
    db.session.commit()
    
    cache.clear()
    # cache.delete('theatre_data_all')
    return jsonify({'success': True}), 200


@app.route('/api/update_theatre', methods=['POST'])
@token_required
def update_theatre():
    data = request.get_json()
    theatre_id = data['theatre_id']
    theatre = Theatre.query.filter_by(id=theatre_id).first()
    theatre.name = data['name']
    theatre.address = data['address']
    theatre.location = data['location']
    theatre.rows = data['rows']
    theatre.cols = data['cols']
    theatre.morning_show_time = data['morning_show_time']
    theatre.matinee_show_time = data['matinee_show_time']
    theatre.first_show_time = data['first_show_time']
    theatre.second_show_time = data['second_show_time']
    db.session.commit()
    # cache.delete('theatre_data')
    # cache.delete('theatre_data_by_id')
    # cache.delete('theatre_data_all')
    cache.clear()

    return jsonify({'success': True}), 200

@app.route('/api/delete_theatre', methods=['POST'])
@token_required
def delete_theatre():
    data = request.get_json()
    id = data['theatre_id']
    theatre = Theatre.query.filter_by(id=id).first()
    db.session.delete(theatre)
    db.session.commit()
    # cache.delete('theatre_data')
    # cache.delete('theatre_data_by_id')
    # cache.delete('theatre_data_all')
    cache.clear()
    return jsonify({'success': True}), 200


@app.route('/api/get_theatre', methods=['GET', 'POST'])
@token_required
def get_venue():
    data = request.get_json()
    admin_id = data['admin_id']
    #cache
    cache_key = f'theatre_data'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    
    theatre = Theatre.query.filter_by(admin_id=admin_id).all()
    theatre_data = []
    for t in theatre:
        theatre_data.append({
            'id': t.id,
            'name': t.name,
            'address': t.address,
            'location': t.location,
            'rows': t.rows,
            'cols': t.cols,
            'morning_show_time': t.morning_show_time,
            'matinee_show_time': t.matinee_show_time,
            'first_show_time': t.first_show_time,
            'second_show_time': t.second_show_time
        })
    #cache
    cache.set(cache_key, theatre_data, timeout=5*60)
    return jsonify(theatre_data)

@app.route('/api/get_theatre_by_id', methods=['GET', 'POST'])
@token_required
def get_venue_by_id():
    data = request.get_json()
    id = data['theatre_id']
    #cache
    cache_key = f'theatre_data_by_id'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    
    theatre = Theatre.query.filter_by(id=id).first()
    theatre_data = {
        'id': theatre.id,
        'name': theatre.name,
        'address': theatre.address,
        'location': theatre.location,
        'rows': theatre.rows,
        'cols': theatre.cols,
        'morning_show_time': theatre.morning_show_time,
        'matinee_show_time': theatre.matinee_show_time,
        'first_show_time': theatre.first_show_time,
        'second_show_time': theatre.second_show_time
    }
    #cache
    cache.set(cache_key, theatre_data, timeout=5*60)
    return jsonify(theatre_data)



@app.route('/api/get_theatre_for_summery', methods=['GET', 'POST'])
@token_required
def get_theatre_for_summery():

    #cache
    cache_key = f'theatre_for_summery'
    cached_data = cache.get(cache_key)
    if cached_data is not None:
        return jsonify(cached_data)
    

    booking = Booking.query.all()
    theatre = Theatre.query.all()
    theatre_data = []
    theatre_name = []
    profit = []
    for t in theatre:
        theatre_name.append(t.name)
        movie = Movie.query.filter_by(theatre_id=t.id).all()
        total_profit = 0
        for m in movie:
            for b in booking:
                if b.movie_id == m.id:
                    total_profit = total_profit + b.total_price
        profit.append(total_profit) 
    theatre_data.append({
        'venue_name': theatre_name,
        'revenue': profit
    })

    #cache
    cache.set(cache_key, theatre_data, timeout=5*60)
    
    return jsonify(theatre_data)
