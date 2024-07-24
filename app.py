from flask import Flask , render_template , request , redirect , url_for ,flash
import string , random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'               #session management, security features
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)