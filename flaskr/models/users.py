# from flaskr.db import create_db as db
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30))
#     last_name = db.Column(db.String(30))
#     bookings = db.relationship("Booking", back_populates="user",cascade="all, delete-orphan")

#     def __init__ (self, name, last_name):
#         self.name = name
#         self.last_name = last_name