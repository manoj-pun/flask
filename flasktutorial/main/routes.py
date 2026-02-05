from flask import render_template, request, Blueprint
from flasktutorial import db
from flasktutorial.models import Post

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page",1,type=int)
    posts = db.paginate(Post.query.order_by(Post.date_posted.desc()),page=page,per_page=2)
    return render_template("home.html", posts=posts)

@main.route("/about")
def about():
    return render_template("about.html", title="About")