from flask import Flask , render_template , request , redirect , url_for ,flash
from flask_sqlalchemy import SQLAlchemy
import string , random
from models import db,URL  # Imported models here to avoid circular imports




def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secretkey'        #session management, security features
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_db.db'
    

    db.init_app(app)            #line links the SQLAlchemy instance (db) with the Flask app (app)

    with app.app_context():             #Ensure that database operations like db.create_all()
                                        #are performed within an application context.
       
        db.create_all()  # Creating tables based on defined models

    app_routes(app)
    return app 





#logic for url shortner

def generate_short_url():                                 #generate random string for short url
      
    characters = string.ascii_letters + string.digits           #includes all alphanumeric chars
    short_url = ''.join(random.choice(characters) for _ in range(6))        #joins the list of characters into a single string, which forms the short URL.
    link = URL.query.filter_by(short_url=short_url).first()                     # queries the URL table for any records with the short_url equal to the newly generated one
                                                                                # and returns the first result
    if link:                                                                #if true , short url exists in db , hence created url is not unique 
        return generate_short_url()                                 #function calls itself recursively to generate a new short_url
                                                                    #until a unique short_url is found

    return short_url        #If no existing link is found (i.e., the short_url is unique), the function returns the short_url.





def app_routes(app):
    #route for index , generating shortend url

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            og_url = request.form['original_url']
            short_url = generate_short_url()
            new_url = URL(og_url= og_url ,short_url = short_url)

            db.session.add(new_url)                 #This line adds the new URL instance to the current database session.
                                                    #This operation prepares the object to be written to the database

            db.session.commit()                     # commits the current transaction to the database

            return render_template('result.html' , short_url= short_url)
        return render_template('index.html')


    #mapping a shortened URL to the original, full UR


    @app.route("/<short_url>")
    def redirect_to_url(short_url):
        link = URL.query.filter_by(short_url=short_url).first_or_404()             #function queries the database to find the entry in the URL table
                                                                    #where the short_url column matches the provided short_url

        return redirect(link.og_url)            #if a matching short_url is found in the db, the func retrieves
                                                #the corresponding original_url from the link object.




if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port =5001)