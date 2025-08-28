from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#for temporary 
head = {"admin":"1234"} # user:password

#tables
class Book(db.Model):# for book entry
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    user = db.Column(db.String(10),default=None)
    date = db.Column(db.Date,default=None)

class Staff(db.Model):# staff add
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    mail = db.Column(db.String(50))
    # password = db.Column(db.String(50))   for simplicity -> halt

class Student(db.Model):# student add
    id = db.Column(db.String(6),primary_key=True)
    name = db.Column(db.String(50))
    passout = db.Column(db.Integer)
    mail = db.Column(db.String(75))

#useful function
data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
   'u', 'v', 'w', 'x', 'y', 'z']
def stu_id(obj): #error found ->lexicography order->solved
    name = obj.name.split()
    yr = (obj.passout) % 100
    ans = str(yr) + name[0][0] + name[-1][0]
    max_id = db.session.query(func.max(Student.id)).filter(Student.id.like(f"{ans}%")).scalar()
    
    if max_id:
        last = max_id[4:] #from index 4 to end
    else:
        return ans + "00"
    
    new_last = ""
    r = 1
    while r >= 0:
        if last[r] == '9':
            new_last = data[0] + new_last #means adding on front
            r -= 1
        else:
            index = data.index(last[r])
            new_last = data[index+1] + new_last
            break

    return ans + last[:r] + new_last



#main
@app.route('/')
def library():
    return render_template("library.html")


#STUDENT
@app.route("/student")
def student():
    return render_template("student.html")


#EMPLOYEE
@app.route("/staff",methods=["POST","GET"])
def staff():
    error = ""
    if request.method=="POST":
        user = request.form["user"]
        fetch = Staff.query.filter_by(name=user).first() #present or not in STAFF TABLE
        if fetch: #present
            staff = user
            return redirect("/staffop")
        else: #adsent
            error = "No such user available"

    return render_template("staff.html",error=error)

@app.route("/staffop")
def Staff_Operation(): #For now COMMON to STAFF
    return render_template("staffop.html")

@app.route("/addstu",methods=["POST","GET"])
def Add_Student():
    if request.method=="POST":
        name=request.form["name"]
        mail=request.form["mail"]
        passout = datetime.now().year + 4
        stu = Student(name=name,mail=mail,passout=passout)
        stu.id = stu_id(stu)
        db.session.add(stu)
        db.session.commit()
        return redirect('/addstu')
    
    all_stu = Student.query.all()
    return render_template("addstu.html",stus=all_stu)

@app.route("/delstu/<id>")
def Del_Student(id):
    useless = Student.query.get(id)
    db.session.delete(useless)
    db.session.commit()
    return redirect("/addstu")


#ADMIN
@app.route("/login",methods=["POST","GET"])
def Admin_Login():
    error = ""
    if request.method == "POST":
        name = request.form["user"]
        password = request.form["password"]
        try:
            if head[name] == password:
                return redirect("/admin")
            else:
                error = "Wrong Password"
        except:
            error = "No such user found"
    
    return render_template("login.html",error=error)


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
  
@app.route("/edel/<int:no>")
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
    app.run(debug=True,host="0.0.0.0")