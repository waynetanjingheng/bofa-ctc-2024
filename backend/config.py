from dotenv import load_dotenv
import os
import secrets

load_dotenv()

DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


class Config(object):
    """Base Class for flask app config"""

    DEBUG = False
    DEVELOPMENT = True
    FLASK_SECRET = os.getenv("FLASK_SECRET_KEY") or secrets.token_hex(16)


class DevConfig(Config):
    """Development environment config"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


class ProdConfig(Config):
    """Production environment config"""

    DEVELOPMENT = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI


# Exported object to load the proper config details depending on the environment.
# Defaults to 'DEFAULT' if no environment is specified.
FLASK_CONFIG = {
    "DEVELOPMENT": DevConfig,
    "PRODUCTION": ProdConfig,
    "DEFAULT": DevConfig,
}
