from flask import Flask


def create_app():
    app = Flask(__name__)
    from src import views, models
    app.config.from_pyfile('config.py')
    app.register_blueprint(views.bp)
    app.register_error_handler(404, views.page_not_found)
    models.db.init_app(app)
    with app.app_context():
        models.db.create_all()
    return app
