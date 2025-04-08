
from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)
    is_complete = db.Column(db.Boolean, default=False)