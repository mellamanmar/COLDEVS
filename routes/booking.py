from flask import Blueprint, render_template, request

booking = Blueprint('booking', __name__)

@booking.route("/booking", methods = ['POST'])
def bookingHome ():
    date = request.form['date']
    name = request.form['name']
    return render_template('booking.html')

@booking.route("/booking/new")
def bookingNew ():
    print ('Save a booking')
    return ('Reserva guardada')

@booking.route("/booking/delete")
def bookingDelete ():
    return 'Reserva cancelada'