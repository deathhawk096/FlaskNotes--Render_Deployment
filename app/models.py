from app import db,loginManager
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer,Serializer
from flask import current_app

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):

    id=db.Column(db.Integer,primary_key=True)

    username = db.Column(db.String(20),unique=True,nullable=False)
    
    email=db.Column(db.String(120),unique=True,nullable=False)

    password=db.Column(db.String(60),nullable=False)

    notes=db.relationship('Notes',backref='author',lazy=True)

    def get_reset_token(self):
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id':self.id})
    
    @staticmethod
    def verify_token(token,expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token,max_age=expires_sec)['user_id']

        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}')"


class Notes(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    title=db.Column(db.String(200),nullable=False)

    content = db.Column(db.String(5000),nullable=False)

    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    user_id= db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    images = db.relationship('Images',backref='note',lazy=True)
                       
    def __repr__(self):
        return f"Notes('{self.id}','{self.title}','{self.content}','{self.user_id}')"

class Images(db.Model):

    id = db.Column(db.Integer,primary_key=True)

    image_url = db.Column(db.String(300),unique=True,nullable=False)

    public_id = db.Column(db.String(200),nullable=False)

    notes_id = db.Column(db.Integer,db.ForeignKey('notes.id'),nullable = False)


    def __repr__(self):
        return f"Images('{self.id}','{self.image_url}','{self.public_id}')"