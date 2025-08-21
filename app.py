from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

head = {"admin":"1234"}

#tables
class Book(db.Model):# for book entry
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
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
    mail = db.Column(db.String(50))
    # password = db.Column(db.String(50))   for simplicity -> halt

class Student(db.Model):# student add
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    year = db.Column(db.Date,default=(datetime.now().year + 1)) 

#useful function
def id_g(cls,name,role):
    year = datetime.now().year % 100
    name_word = name.split()
    letter = name_word[0][0] + name_word[-1][0]
    prefix = str(year) + letter + role
    obj = cls.query.filter(cls.id.like(f"{prefix}%")).order_by(desc(cls.id)).first()
    
    if obj:
        last = obj.id[-1] #not always, exception for more digit number
        return f"{prefix}{int(last)+1}"
    
    return prefix+"0"




#main
@app.route('/')
def library():
    return render_template("library.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route("/admin",methods=["GET","POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        mail = request.form["mail"]
        emp_add = Staff(name=name,mail=mail)
        db.session.add(emp_add)
        db.session.commit()
        return redirect("/admin")
    
    return render_template("admin.html",emp = Staff.query.all())


    
@app.route("/edel/<int:no>",methods=["POST","GET"])
def Employee_Del(no):
    emp_fetch = Staff.query.get(no)
    db.session.delete(emp_fetch)
    db.session.commit()
    return redirect("/admin")


@app.route("/abtus")
def About_Us():
    return render_template("abtus.html")

@app.route("/cnt")
def contact():
    return render_template("cnt.html")
    

if __name__== "__main__":
    with app.app_context(): db.create_all()
    app.run(debug=True)