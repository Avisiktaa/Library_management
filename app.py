from flask import Flask,render_template

app = Flask(__name__)

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
    app.run(debug=True)