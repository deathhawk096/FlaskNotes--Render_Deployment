from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import cloudinary
#from flask_mail import Mail
import os
from app.config import Config

db=SQLAlchemy()
migrate=Migrate()
bcrypt = Bcrypt()
loginManager = LoginManager()
#mail = Mail()


loginManager.login_view = 'login'
loginManager.login_message = 'Please Log In To Access That Page'
loginManager.login_message_category = 'info'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    loginManager.init_app(app)
    #mail.init_app(app)

    cloudinary.config(
        cloud_name = app.config['CLOUDINARY_CLOUD_NAME'],
        api_key = app.config['CLOUDINARY_API_KEY'],
        api_secret = app.config['CLOUDINARY_API_SECRET']
        )

    from app.main.main_routes import main
    from app.notes.note_routes import notes
    from app.users.users_routes import users
    from app.error.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(notes)
    app.register_blueprint(users)
    app.register_blueprint(errors)

    return app