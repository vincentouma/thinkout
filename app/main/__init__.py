from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
main = Blueprint('main',__name__)
from . import views,error
