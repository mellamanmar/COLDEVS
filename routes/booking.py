from flask import Blueprint

booking = Blueprint('booking', __name__)

@booking.route("/booking")
def bookingHome ():
    return 'Usuarios que tienen reservas'

@booking.route("/booking/new")
def bookingNew ():
    return 'Nueva reserva'

@booking.route("/booking/delete")
def bookingDelete ():
    return 'Reserva cancelada'