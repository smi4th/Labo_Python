from app import db
import datetime
from flask_login import UserMixin

class Forum(db.Model):
    __bind_key__ = 'forum'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')

    def __repr__(self):
        return 'Forum ' + str(self.id)

class MessageInForum(db.Model):
    __bind_key__ = 'messageInForum'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    forum_id = db.Column(db.Integer, db.ForeignKey('forum.id'), nullable=False)
    forum = db.relationship('Forum', backref=db.backref('messages', lazy=True))

    def __repr__(self):
        return 'MessageInForum ' + str(self.id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return 'User ' + str(self.id)
