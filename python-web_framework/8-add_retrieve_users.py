from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

############################# TO DO 1 ############################
# Add your code to connect to the database here
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
db = SQLAlchemy(app)
###############################################################

############################ TO DO 2 ##############################
# Define your USER Model class here
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
#################################################################

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()  # This calls the function to create tables


@app.route('/', strict_slashes=False)
def index():
    return "Hello, ALX Flask!"

@app.route('/add_user' ,methods=['GET','POST'], strict_slashes=False)
def addUser():

    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')

            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()

            flash('User added successfully!','success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {str(e)}','error')
        return render_template('add_user.html')
@app.route('/users')
def users():
    all_users=User.query.all()
    return render_template('users.html',users=all_users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
