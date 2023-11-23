from flask import Flask
from flask_bootstrap import Bootstrap5
from decouple import config
from routes import main_bp
from os import urandom


def create_app() -> Flask:
    """
    Create and configure the Flask applicat ion.

    Returns:
        Flask: The configured Flask application.
    """

    app = Flask(__name__)
    Bootstrap5(app)
    app.register_blueprint(main_bp)

    db_host = config('DB_HOST')
    db_user = config('DB_USER')
    db_password = config('DB_PASSWORD')
    db_name = config('DB_NAME')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{db_user}:{db_password}@{db_host}/{db_name}'
    app.config['SECRET_KEY'] = urandom(32)

    return app


