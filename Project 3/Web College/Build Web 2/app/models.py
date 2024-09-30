from . import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)  # Store the hashed password
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp for account creation

    def __repr__(self):
        return f'<User {self.username}>'
