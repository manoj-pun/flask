import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flasktutorial.config import Config


# Create a new Flask web application
# 'app' is the variable that stores our Flask app object
# '__name__' tells Flask that this file is the main program
# Flask uses this to know where to look for templates and static files
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "users.login"
login_manager.login_message_category = "info"

mail = Mail(app)

from flasktutorial.models import User

# print("MAIL USER:", app.config["MAIL_USERNAME"])
# print("MAIL PASS LENGTH:", len(app.config["MAIL_PASSWORD"]) if app.config["MAIL_PASSWORD"] else None)

from flasktutorial.users.routes import users
from flasktutorial.posts.routes import posts
from flasktutorial.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
