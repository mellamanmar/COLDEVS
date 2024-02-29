from utils.db import db

class Booking(db.Model):
    __tablename__ = 'Reservas'
    booking_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('User', back_populates="bookings", uselist=False, single_parent=True)
    