from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String())
    comments = db.relationship("Comment", backref = "comments", lazy = "dynamic")


    def save_user(self):
        db.session.add(self)
        db.session.commit()


    @property
    def password(self):
        raise AttributeError("oya...jibebebe..siujibebebebe")

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash ,password)

    def get_user_pitches(self):
        user = User.query.filter_by(id = self.id).first()
        return user.pitches

    def get_user_comments(self):
        user  = User.query.filter_by(id = self.id).first()
        return user.comments