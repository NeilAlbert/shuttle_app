# Student Shuttle Booking System

A web-based shuttle booking system built with **Flask**, **SQLite**, and **Bootstrap**.  
It allows students to book seats for different locations with options for Regular, VIP, and VVIP tickets.  
Administrators can monitor all bookings in real time.  

---

## Features
- Student booking form with:
  - Name, Student ID, Department
  - Destination selection (Cape Coast, Koforidua, Kumasi, Ho)
  - Ticket type selection (Regular, VIP, VVIP)
- Automatic fare calculation:
  - Cape Coast → Regular: 60, VIP: 70, VVIP: 80  
  - Koforidua → Regular: 50, VIP: 60, VVIP: 70  
  - Kumasi → Regular: 120, VIP: 135, VVIP: 140  
  - Ho → Regular: 150, VIP: 160, VVIP: 170  
- Capacity limit of **50 students per location**.  
- Success page showing booking confirmation and fare.  
- Admin dashboard listing all bookings.  
- Responsive design with Bootstrap.  

---

## Technologies Used
- [Python 3.10](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)  
- [SQLite](https://www.sqlite.org/)  
- [Bootstrap 5](https://getbootstrap.com/)  
- [Gunicorn](https://gunicorn.org/) (for deployment)  

---

##   Project Structure
```
shuttle_app/
│── app.py               # Main Flask application
│── requirements.txt     # Python dependencies
│── Procfile             # Deployment file for Render/Heroku
│── runtime.txt          # Python version for deployment
│── static/
│   └── style.css        # Custom styles
│── templates/
│   ├── index.html       # Booking form
│   ├── success.html     # Booking confirmation page
│   └── admin.html       # Admin dashboard
```

---

##  Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shuttle_app.git
   cd shuttle_app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Mac/Linux
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Deployment (Render / Heroku)

1. Push your project to GitHub.  
2. On [Render](https://render.com) or [Heroku](https://www.heroku.com/):
   - Connect to your GitHub repo.  
   - Set **Build Command**:  
     ```bash
     pip install -r requirements.txt
     ```
   - Set **Start Command**:  
     ```bash
     gunicorn app:app
     ```
3. Deploy 

---

##  Group Members
- Baah Frimpong – Backend Development  
- Amponsah Michael Halagbe – Database Management  
- Nana Ato Dadzie – Frontend Design  
- Osam Theodora – Styling & Responsiveness  
- Forson Albert Ofori-Yaw – Deployment & Documentation  

---

## License
This project is for academic purposes.   
