from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Create a new Flask web application
# 'app' is the variable that stores our Flask app object
# '__name__' tells Flask that this file is the main program
# Flask uses this to know where to look for templates and static files
app = Flask(__name__)

app.config["SECRET_KEY"] = "d70c9ffca4a02b6a78d8185357e6424a"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["WTF_CSRF_ENABLED"] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

from flasktutorial.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from flasktutorial import routes
