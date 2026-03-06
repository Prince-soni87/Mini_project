import os
from flask import Flask
from .extensions import db, login_manager, bcrypt
from config import Config

from .auth.routes import auth_bp
from .main.routes import main_bp
from .api import api_bp


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Correct upload folder using absolute path
    upload_folder = os.path.join(app.root_path, "static", "uploads")

    # create folder automatically if missing
    os.makedirs(upload_folder, exist_ok=True)

    app.config["UPLOAD_FOLDER"] = upload_folder

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    with app.app_context():
        db.create_all()

    return app