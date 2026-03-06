from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))