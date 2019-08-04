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
