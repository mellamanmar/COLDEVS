# from .. import db
# from sqlalchemy import inspect
# from datetime import datetime
# from sqlalchemy.orm import validates


# class Booking(db.Model):
#     __tablename__ = 'Reservas'
#     booking_id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.Date)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
#     user = db.relationship(User, back_populates="bookings", uselist=False, single_parent=True)
    
#     def __init__(self, date, user):
#         self.date = date
#         self.user = user