from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()


class Data(db.Model):
    form_id = db.Column(db.Integer, primary_key=True)
    form_data = db.Column(JSONB)
    time_create = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.form_id}: {self.form_data}'
