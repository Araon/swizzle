from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '7ef110cbba2b2d844d791a38b689fc85'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
'''
The routes are imported after the database is created because 
it may led to circular import in python which is not good
'''
from swizzle import routes

