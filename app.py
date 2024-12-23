#!/usr/bin/env python3

# Standard library imports
import os

# Remote library imports
from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from models import PetOwner, PetSitter, Appointment
from config import db, api  # You can import the api object if using Flask-Restful

# Flask app initialization
app = Flask(__name__)

# Set up the base directory and database path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "instance", "app.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

# Initialize the database and migration extension
db.init_app(app)
migrate = Migrate(app, db)

# Views go here!
@app.route('/')
def index():
    return '<h1>Project Server</h1>'

if __name__ == '__main__':
    # Ensure the instance folder exists
    os.makedirs(os.path.join(BASE_DIR, 'instance'), exist_ok=True)
    app.run(port=5555, debug=True)






















# #!/usr/bin/env python3

# # Standard library imports



# # Remote library imports
# from flask import request
# from flask_restful import Resource

# # Local imports
# from config import app, db, api
# # Add your model imports


# # Views go here!

# @app.route('/')
# def index():
#     return '<h1>Project Server</h1>'


# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

