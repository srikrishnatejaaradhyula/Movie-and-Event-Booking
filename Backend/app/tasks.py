
from app import  celery
from celery import Celery
from celery.schedules import crontab
from celery.utils.log import get_task_logger

from .mail import send_email

from .model import Booking, AdminAuth, UserAuth , Theatre,Movie


from datetime import datetime, timedelta


import os
import csv
import time 




@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # sender.add_periodic_task(
    #     10.0, test.s('world'), expires=4
    # ),
    #monthly report
    sender.add_periodic_task(
        crontab(day_of_month='1', hour=23, minute=59),
        send_monthly_report.s(),
    ),
    #daily remainder
    sender.add_periodic_task(
        crontab(hour=18, minute=00),
        send_daily_remainder.s(),
    ),
    sender.add_periodic_task(
        60.0,  # Run every 60 seconds (adjust the interval as needed)
        add_booking_remainder_tasks.s(),
    ),
      
    #test 
    sender.add_periodic_task(
        crontab(month_of_year='11',day_of_month='2',hour=19,minute=58),
        a_20_sec_task.s(),
    )





@celery.task
def send_monthly_report():
    data = get_booking_report_current_month()
    with open('monthly_bookings.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    auth = AdminAuth.query.all()
    for a in auth:
        send_email("mad2project.ticketshow@gmail.com",a.email,"Monthly Report", "Please find the attached monthly report", "monthly_bookings.csv")
    





def get_booking_report_current_month():
    today = datetime.today()
    first_day_of_month = today.replace(day=1,month=today.month-1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = first_day_of_month.replace(month=today.month) - timedelta(days=1)

    bookings = Booking.query.filter(Booking.booking_time >= first_day_of_month,
                                Booking.booking_time <= last_day_of_month).all()
    all_bookings = [
        ["Booking ID", "Show Name", "Booking Time", "Seats", "Rating", "Venue Name", "Venue Location"]
    ]
    for b in bookings:
        movie = Movie.query.filter_by(id=b.movie_id).first()
        theatre = Theatre.query.filter_by(id=movie.theatre_id).first()

        all_bookings.append([
            b.id,
            movie.name,
            b.booking_time,
            b.seats,
            b.rating,
            theatre.name,
            theatre.address,
        ])
    return all_bookings



@celery.task
def send_daily_remainder():
    auth = AdminAuth.query.all()
    for a in auth:
        if a.last_login == None:
            continue
        if a.last_login.date() == datetime.today().date():
                continue
        
        send_email("mad2project.ticketshow@gmail.com",a.email,"Daily Reminder", "Please visit the admin dashboard, You are not visited today")



@celery.task
def send_booking_remainder(email, booking_id):
    booking = Booking.query.filter_by(id=booking_id).first()
    movie = Movie.query.filter_by(id=booking.movie_id).first()
    theatre = Theatre.query.filter_by(id=movie.theatre_id).first()
    send_email.apply_async(("mad2project.ticketshow@gmail.com",email,"Booking Reminder", "Your booking is scheduled on "+booking.movie_date+" at "+booking.movie_time+" for "+movie.name+" at "+theatre.name+" "+theatre.address))



@celery.task
def add_booking_remainder_tasks():
    bookings = Booking.query.all()
    for b in bookings:
        user = UserAuth.query.filter_by(id=b.user_id).first()
        email = user.email
        id = b.id
        given_datetime = datetime.strptime(f"{b.movie_date} {b.movie_time}", "%Y-%m-%d %H:%M")
        
        # Subtract 1 hour from the given datetime
        given_datetime -= timedelta(hours=1)

        # Get the current datetime
        current_datetime = datetime.now()

        given_time = given_datetime.strftime("%H:%M")
        current_time = current_datetime.strftime("%H:%M")
        given_date = given_datetime.strftime("%Y-%m-%d")
        current_date = current_datetime.strftime("%Y-%m-%d")


        # Check if the two datetime objects are equal
        if given_time == current_time and given_date == current_date:
            print("Equal" + str(given_time)+" "+str(current_time))
            send_booking_remainder.apply_async((email, id) )
        else:
            print("Not equal"+str(given_time)+" "+str(current_time))













@celery.task
def add(x, y):
    print("add")
    return x + y

@celery.task
def test(arg):
    print("test")
    print(arg)
    return arg

@celery.task
def a_20_sec_task():
    print("20 sec task")
    time.sleep(20)
    print("20 sec task done")