from flask import render_template, flash, url_for, request,redirect
from swizzle import app
from swizzle.forms import RegistrationForm, LoginForm


@app.route("/")
def index():
    return render_template('home.html')

@app.route("/login", methods=["POST","GET"])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route("/play")
def play():
    return render_template('gamepage.html')


@app.route("/error")
def error():
    return render_template('errorpage.html')