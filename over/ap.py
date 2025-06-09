#1 
from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid " ,mimetype="text/plain")
    
    return ''' 
           <h2>Login page</h2>
           <form method = "POST">
           username: <input type="text" name="username"><br>
           password: <input type="text" name="password"><br>
           <input type="submit" value="Login">
           </form>

'''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
                 <h2> welcome , {session["user"]}!</h2>
                 <a hred={url_for( 'logout' )}>Logout</a>
'''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# 2 

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "heloo every one here"

@app.route("/about")
def about():
    return "my name is aditi gupta"

@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST" :
        return "given a data"
    else :
        return "jusst reaeding"
    

# 3 

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def student_profile():
    return render_template(
        "profile.html",
        name = "aditi",
        is_topper = True,
        subjects = ["maths", "science" , "cs"]
    )
