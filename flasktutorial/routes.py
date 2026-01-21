from flask import render_template, url_for,flash,redirect
from flasktutorial import app, db, bcrypt
from flasktutorial.forms import RegistrationForm, LoginForm
from flasktutorial.models import User, Post

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Your account has been created! You are now able to login","success")
        return redirect(url_for("login"))
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