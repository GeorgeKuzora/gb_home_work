from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    surname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, surname, email, password) -> None:
        self.name = name
        self.surname = surname
        self.email = email
        self.password = bcrypt.generate_password_hash(password)
        self.created_at = datetime.utcnow()

    def __repr__(self) -> str:
        return f"User({self.name}, {self.surname}, {self.email}, {self.password})"
