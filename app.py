from flask import Flask, render_template, request, redirect, url_for
import sqlite3

DATABASE = "book.db"
app = Flask(__name__)

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS books(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER NOT NULL
                )
            """
        )
        conn.commit()

def get_db_connection():
    """Get Database Connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_all_books():
    """Fetch all books from database"""
    conn = get_db_connection()
    books_list = conn.execute('SELECT * FROM books ORDER BY id').fetchall()
    conn.close()
    return books_list

def add_book_to_db(title, author, year):
    """Add a new book to database"""
    conn = get_db_connection()
    conn.execute('INSERT INTO books(title,author, year) VALUES(?,?,?)',
                 (title, author, year))
    conn.commit()
    conn.close()

def delete_book_from_db(book_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    book_list = get_all_books()
    print(book_list)
    return render_template('index.html', books = book_list)


@app.route('/add-book')
def add_book():
    return render_template('add_book.html')

@app.route("/greet", methods=['POST'])
def greet():
    user_name = request.form['title']
    author = request.form['author']
    year = request.form['year']

    add_book_to_db(title=user_name, author = author, year=year)
    return redirect(url_for("index"))

@app.route("/delete/<book_id>", methods=['POST'])
def delete_book(book_id):
    delete_book_from_db(book_id)
    return redirect("/")

@app.route("/book_detail/<book_id>")
def book_details(book_id):
    """Challenge"""
    return render_template('books_details.html' , book = [])


if __name__ == '__main__':
    init_db()
    app.run(debug=True)