-- Create a table for storing books
CREATE TABLE IF NOT EXISTS book (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publication_date DATE NOT NULL,
    genre VARCHAR(50),
    isbn VARCHAR(20) UNIQUE NOT NULL
);
