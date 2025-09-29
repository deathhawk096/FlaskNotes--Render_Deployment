from flask import Blueprint,render_template
from flask_login import login_required,current_user
from app.models import Notes

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/webpage')
def webpage():
    return render_template("webpage.html",title='wen Page')

@main.route("/home")
@login_required
def home():
    notes = Notes.query.filter_by(user_id=current_user.id).order_by(Notes.date_posted.desc())
    return render_template("home.html",title='Home Page',notes=notes)