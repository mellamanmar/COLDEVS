# from flask import (
#     Blueprint, flash, g, redirect, render_template, request, url_for
# )
# from flask_sqlalchemy import SQLAlchemy
# from flaskr.models.booking import Booking

# db = SQLAlchemy()

# booking = Blueprint('booking', __name__)

# @booking.route("/booking")
# def bookingHome ():
#     booking = db.session.execute(db.select(Booking).order_by(Booking.user).scalars())
#     return render_template('booking.html', bookings = booking)

# @booking.route("/booking/new", methods = ['GET', 'POST'])
# def bookingNew ():
#     # date = request.form['date']
#     # user = request.form['name']

#     new_booking = Booking (date, user)
#     return 'Reserva guardada'

# @booking.route("/booking/delete")
# def bookingDelete ():
#     return 'Reserva cancelada'