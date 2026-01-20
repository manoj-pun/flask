from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Create a new Flask web application
# 'app' is the variable that stores our Flask app object
# '__name__' tells Flask that this file is the main program
# Flask uses this to know where to look for templates and static files
app = Flask(__name__)
# print(__name__)

app.config["SECRET_KEY"] = 'd70c9ffca4a02b6a78d8185357e6424a'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from flasktutorial import routes