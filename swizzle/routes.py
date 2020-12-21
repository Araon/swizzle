from flask import render_template, url_for, request
from swizzle import app
from swizzle.database import insert_data


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pwd"]

    else:
        return render_template('login.html')

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["pwd"]
        email = request.form["email"]

        insert_data(username,password,email)
        return "<a href='/'>Back</a>"
    else:
        return render_template('register.html')
    

@app.route("/play")
def play():
    return render_template('gamepage.html')