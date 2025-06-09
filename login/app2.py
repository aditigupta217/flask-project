from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/submit", methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    '''if username =="aditi" and password == "pass":
        return render_template("welcome.html")'''
    
    valid_user = {
        'aditi':'123',
        'nikita': 'Nikita@432'
    }
 
    if username in valid_user and password == valid_user[username]:
        return render_template("welcome.html", name = username)
    else:
        return "invalid  page"
    
