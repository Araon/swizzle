from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '7ef110cbba2b2d844d791a38b689fc85'

from swizzle import routes

