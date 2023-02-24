from flask import Flask
from views import bp, page_not_found
from models import db


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_pyfile('config.py')
    flask_app.register_blueprint(bp)
    flask_app.register_error_handler(404, page_not_found)
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()
    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=False)
