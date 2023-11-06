from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="app/templates")
    app.config.from_object(config_class)

    db.init_app(app)

    # Import and register your blueprints here
    # from .views import your_blueprint
    # app.register_blueprint(your_blueprint)

    return app
