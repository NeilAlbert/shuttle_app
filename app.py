#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flask Shuttle Booking Webapp
"""

import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "supersecretkey"  # change this for production

# Database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "shuttle.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize database
db = SQLAlchemy(app)

# Booking Model
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    student_id = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    ticket_type = db.Column(db.String(20), nullable=False)
    fare = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Booking {self.name} - {self.location}>"

# Fares and limits
fares = {
    "Cape Coast": {"Regular": 60, "VIP": 70, "VVIP": 80},
    "Koforidua": {"Regular": 50, "VIP": 60, "VVIP": 70},
    "Kumasi": {"Regular": 120, "VIP": 135, "VVIP": 140},
    "Ho": {"Regular": 150, "VIP": 160, "VVIP": 170}
}
max_capacity = 50

# Create database if not exists
if not os.path.exists(db_path):
    with app.app_context():
        db.create_all()

# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        student_id = request.form["student_id"]
        department = request.form["department"]
        location = request.form["location"]
        ticket_type = request.form["ticket_type"]

        # Validate location and ticket
        if location not in fares or ticket_type not in fares[location]:
            flash("Invalid location or ticket type.")
            return redirect(url_for("index"))

        # Check seat availability
        current_count = Booking.query.filter_by(location=location).count()
        if current_count >= max_capacity:
            flash(f"Sorry, {location} shuttles are fully booked!")
            return redirect(url_for("index"))

        # Get fare
        fare = fares[location][ticket_type]

        # Save booking
        new_booking = Booking(
            name=name,
            student_id=student_id,
            department=department,
            location=location,
            ticket_type=ticket_type,
            fare=fare
        )
        db.session.add(new_booking)
        db.session.commit()

        return render_template("success.html", booking=new_booking, fares=fares)

    return render_template("index.html", fares=fares)

@app.route("/admin")
def admin():
    bookings = Booking.query.all()
    return render_template("admin.html", bookings=bookings)

# Run server
if __name__ == "__main__":
    app.run(debug=False)
