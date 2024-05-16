#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    title = data.get('title')
    author = data.get('author')
    if title and author:
        try:
            new_book = Book(title=title, author=author)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({'message': 'Book added successfully'}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Book title already exists'}), 400
    else:
        return jsonify({'error': 'Title and author are required'}), 400

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.json
    title = data.get('title', book.title)
    author = data.get('author', book.author)
    book.title = title
    book.author = author
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
