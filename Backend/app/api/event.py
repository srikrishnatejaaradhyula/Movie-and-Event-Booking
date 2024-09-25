from flask import request, jsonify, send_file
from app import app, db , cache
from app.token import token_required
from app.model import Event,EventBooking,UserAuth
from datetime import datetime
from base64 import b64decode, b64encode
from app.mail import send_email,send_email_html
from json import dumps,loads
import io


@app.route('/api/create_event', methods=['POST','GET'])
# @token_required
def create_event():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    name = data['name']
    description = data['description']
    location = data['location']
    address = data['address']
    date = data['date']
    form = data['form']
    price = data['price']
    admin_id = data['admin_id']
    file = data['file']
    file = b64decode(file)
    event = Event(name=name, description=description, location=location, address=address, date=date, form=dumps(form), price=price, admin_id=admin_id, brochure=file)
    db.session.add(event)
    db.session.commit()
    cache.clear()
    return jsonify({'success': True}), 200

@app.route('/api/update_event', methods=['POST'])
@token_required
def update_event():
    data = request.get_json()
    id = data['id']
    event = Event.query.filter_by(id=id).first()
    name = data['name']
    description = data['description']
    location = data['location']
    address = data['address']
    date = data['date']
    form = data['form']
    price = data['price']
    admin_id = data['admin_id']
    event.name = name
    event.description = description
    event.location = location
    event.address = address
    event.date = date
    event.form = dumps(form)
    event.price = price
    event.admin_id = admin_id
    if data['file']:
        event.brochure = b64decode(data['file'])
    db.session.commit()
    cache.clear()
    return jsonify({'success': True}), 200

@app.route('/api/delete_event', methods=['POST'])
@token_required
def delete_event():
    data = request.get_json()
    id = data['id']
    event = Event.query.filter_by(id=id).first()
    db.session.delete(event)
    db.session.commit()
    cache.clear()
    return jsonify({'success': True}), 200


@app.route('/api/get_event_all', methods=['GET', 'POST'])
@token_required
def get_event_all():
    #cache
    cache_key = 'event_data_all'
    event_data = cache.get(cache_key)
    if event_data:
        return jsonify(event_data)

    event = Event.query.all()
    event_data = []
    for e in event:
        event_data.append({
            'id': e.id,
            'name': e.name,
            'description': e.description,
            'location': e.location,
            'address': e.address,
            'date': e.date,
            'form': loads(e.form),
            'price': e.price,
            'admin_id': e.admin_id
        })
    cache.set(cache_key, event_data, timeout=5 * 60)
    return jsonify(event_data)


@app.route('/api/get_brochure', methods=['GET', 'POST'])
def get_brochure():
    data = request.get_json()
    id = data['id']
    event = Event.query.filter_by(id=id).first()
    return send_file(
        io.BytesIO(event.brochure),
        attachment_filename='brochure.pdf',
        mimetype='application/pdf'
    )

@app.route('/api/get_event_by_id', methods=['GET', 'POST'])
@token_required
def get_event_by_id():
    data = request.get_json()
    event_id = data['id']
    event = Event.query.filter_by(id=event_id).first()
    event_data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'location': event.location,
        'address': event.address,
        'date': event.date,
        'form': loads(event.form),
        'price': event.price,
        'admin_id': event.admin_id
    }
    return jsonify(event_data)

@app.route('/api/book_event', methods=['GET', 'POST'])
@token_required
def book_event():
    data = request.get_json()
    event_id = data['id']
    user_id = data['user_id']
    form = data['form']
    price = data['price']
    booking_time = datetime.now()
    event = Event.query.filter_by(id=event_id).first()
    user = UserAuth.query.filter_by(id=user_id).first()
    booking = EventBooking(form=dumps(form), price=price, booking_time=booking_time, event_id=event_id, user_id=user_id)
    send_email_html("mad2project.ticketshow@gmail.com",user.email, 'Booking Confirmation', """<h1>Booking Confirmation</h1><br><p>Thank you for booking with us. Your booking is confirmed. Please visit the event venue on time.</p>""")
    db.session.add(booking)
    db.session.commit()
    cache.clear()
    return jsonify({'success': True}), 200

@app.route('/api/get_event_and_booking',methods=['POST'])
@token_required
def get_event_and_booking():
    data = request.get_json()
    event_id = data['event_id']
    events = EventBooking.query.filter_by(event_id=event_id).all()
    event_data = []
    for e in events:
        user = UserAuth.query.filter_by(id=e.user_id).first()
        event = Event.query.filter_by(id=event_id).first()
        data1 = {
            'user_name' : user.name,
            'event_reg_date':e.booking_time,
        }
        form = loads(e.form)
        for f in form:
            data2 = {
                f["name"] : f["value"]
            }
            data1.update(data2)
        event_data.append(data1)
    return jsonify(event_data)


@app.route('/api/update_event_rating', methods=['GET', 'POST'])
@token_required
def update_event_rating():
    data = request.get_json()
    booking_id = data['event_id']
    rating = data['rating']
    booking = EventBooking.query.filter_by(id=booking_id).first()
    booking.rating = rating
    #cache
    # cache.delete('booking_data')
    # cache.delete('booking_data_by_id')

    cache.clear()

    db.session.commit()
    return jsonify({'success': True}), 200

@app.route('/api/get_user_event_booking',methods=['POST'])
@token_required
def get_user_event_booking():
    data = request.get_json()
    user_id = data['user_id']
    event_booking = EventBooking.query.filter_by(user_id=user_id).all()
    event_data = []
    for e in event_booking:
        event = Event.query.filter_by(id=e.event_id).first()
        event_data.append({
            'name':event.name,
            'location':event.location,
            'address': event.address,
            'date': event.date,
            'rating': e.rating,
            'price':e.price,
            'id':e.id
        })
    return jsonify(event_data)