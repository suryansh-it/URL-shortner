from app import db

class URL():                                    #database model for URL
    __tablename__ = 'url'
    id = db.Column(db.Integer, primary_key=True)
    og_url = db.Column(db.String(200), nullable=False)              #CANT BE NULL
    short_url = db.Column(db.String(10), nullable=False, unique=True)   #STORED URL SHOULD BE UNIQUE
    date_creation = db.Columnn(db.DateTime, default=db.func.now())          



