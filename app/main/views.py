from ..models import User,Pitch,Comment
from flask import render_template,redirect,url_for,request,abort
from . import main
import datetime
from app.models import User, Pitch
from flask_login import login_required
from .. import db,photos
from .forms import AddPitchForm,AddComment,UpdateProfile



@main.route("/")
def index():
    pitches = Pitch.query.all()
    title = "Home"
    return render_template("index.html", pitches = pitches,title = title)

@main.route("/pitches/<category>")
def categories(category):
    # pitches = None
    if category == "all":
        pitches = Pitch.query.all()
    else:
        pitches = Pitch.query.filter_by(category = category).all()

    return render_template("pitches.html", pitches = pitches, title = category)




    @main.route("/<uname>/add_pitch", methods = ["GET","POST"])
@login_required
def add_pitch(uname):
    form = AddPitchForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    title = "Add Pitch"
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data 
        dateOriginal = datetime.datetime.now()
        time = str(dateOriginal.time())
        time = time[0:5]
        date = str(dateOriginal)
        date = date[0:10]
        new_pitch = Pitch(title = title, pitch = pitch, category = category,user_id = user.id)
        new_pitch.save_pitch()
        pitches = Pitch.query.all()
        return redirect(url_for("main.categories",category = category))
    return render_template("add_pitch.html",form = form, title = title)

