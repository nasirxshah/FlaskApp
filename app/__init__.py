from flask import Flask

from app.api import api_bp
from app.extensions import mongo
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    # add configurations
    app.config.from_object(config_class)

    # Initialize Flask extensions
    mongo.init_app(app)

    # Register blueprints
    app.register_blueprint(api_bp)

    return app