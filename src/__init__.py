from flask import Flask

from .models.models import db
from .views import views
from .views.views import page_not_found


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(views.bp)
    app.register_error_handler(404, page_not_found)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
