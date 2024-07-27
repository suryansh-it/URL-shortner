from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URL(db.Model):                                    #database model for URL
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    og_url = db.Column(db.String(200), nullable=False)              #CANT BE NULL
    short_url = db.Column(db.String(10), nullable=False, unique=True)   #STORED URL SHOULD BE UNIQUE
    date_creation = db.Column(db.DateTime, default=db.func.now())          

    



