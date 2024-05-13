from flask import Flask
import os
from dotenv import load_dotenv
from config import FLASK_CONFIG
# from database.database import db, ma
from routes import api

# Create the application using the application factory pattern.
# For more information, visit https://flask.palletsprojects.com/en/3.0.x/patterns/appfactories/.


def create_flask_app(config_environment: str = "DEFAULT") -> Flask:
    """Creates the flask app instance based on the environment specified.

    Args:
        config_environment (str): "DEVELOPMENT" or "PRODUCTION"

    Returns:
        Flask: an instance of the Flask application
    """

    app = Flask(__name__)
    app.config.from_object(FLASK_CONFIG.get(config_environment))
    # db.init_app(app=app)
    # ma.init_app(app=app)
    app.register_blueprint(api, url_prefix="/api")
    return app


if __name__ == "__main__":
    load_dotenv()

    app = create_flask_app(config_environment=os.getenv("FLASK_CONFIG", "DEFAULT"))
    app.run(port=os.getenv("FLASK_RUN_PORT"))
