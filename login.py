from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
import sqlite3

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

# ---------------------------------LOGIN SETUP------------------------------------------

db = SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#set the type and location of the DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sw.db'
#make sure this key stays secret
app.config['SECRET_KEY'] = 'key'


#class name has to match the table name
#class variables must match the column names of the table
#one column must be called 'id'
class Uzers(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uzername = db.Column(db.String)
    password = db.Column(db.String)

#should be set to refer to the class name as above
@login_manager.user_loader
def load_user(id):
    return Uzers.query.get(id)

