from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# Initialize the database object
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object(config_class)

    # Initialize the database
    db.init_app(app)

    # Register routes
    from app.routes import main
    app.register_blueprint(main)

    return app
