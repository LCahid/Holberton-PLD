from datetime import datetime
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publication_date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    genre = db.Column(db.String(50))
    isbn = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.publication_date}', '{self.genre}', '{self.isbn}')"
