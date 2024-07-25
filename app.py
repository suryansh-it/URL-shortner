from flask import Flask , render_template , request , redirect , url_for ,flash
import string , random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'               #session management, security features
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///url_db.db'



db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)