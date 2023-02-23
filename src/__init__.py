from flask import Flask
from views import bp, page_not_found
from models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(bp)
    app.register_error_handler(404, page_not_found)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
