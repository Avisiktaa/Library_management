from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

head = {"admin":"1234"}

class Book(db.Model):# for book entry
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    price = db.Column(db.Integer)
    user = db.Column(db.String(10),default=None)
    date = db.Column(db.Date,default=None)

class Stock(db.Model): #student will search the book
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    count = db.Column(db.Integer)

class Staff(db.Model):# staff add
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Student(db.Model):# staff add
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))

    

@app.route('/')
def library():
    return render_template("library.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")
    
@app.route("/abtus")
def About_Us():
    return render_template("abtus.html")

@app.route("/cnt")
def contact():
    return render_template("cnt.html")
    

if __name__== "__main__":
    #with app.app_context(): db.create_all()
    app.run(debug=True)