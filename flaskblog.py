from datetime import datetime
from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default="default.jpg")
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship("Post",backref="author",lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"),nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

posts = [
    {
        "title":"Post 1",
        "author":"Manoj Pun",
        "date_posted":"2025-11-12",
        "content":"First Blog Post"
    },
    {
        "title":"Post 2",
        "author":"Jane Doe",
        "date_posted":"2022-11-12",
        "content":"Second Blog Post"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for("home"))
    return render_template("register.html",title="Register",form=form)

@app.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "manoj@gmail.com" and form.password.data == "password":
            flash("You have logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful","danger")
    return render_template("login.html",title="Login",form=form)

if __name__ == "__main__":
    app.run(debug=True)
