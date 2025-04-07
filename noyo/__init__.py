from flask import Flask
from .extensions import db
from .api.persons import persons_bp
import os


def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/noyo"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(persons_bp)

    # Import models after db initialization
    from .models.person import Person
    from .models.segment import Segment

    return app
