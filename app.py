from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


#book array
books = [
    {"id" : 1, "title": "Harry Potter","author":"JK Rowling", "year": 1995 },
{"id" : 2, "title": "A song of ice and fire","author":"George Martin", "year": 2000 },
]


@app.route('/home')
def index():
    return render_template('index.html', books = books)


@app.route('/add-book')
def add_book():
    return render_template('add_book.html')

@app.route("/greet", methods=['POST'])
def greet():
    user_name = request.form['title']
    author = request.form['author']
    year = request.form['year']
    book_id = len(books) + 1
    book = {
        "id": book_id,
        "title": user_name,
        "author": author,
        "year": year
    }
    books.append(book)
    return redirect(url_for("index"))

@app.route("/delete/<book_id>", methods=['POST'])
def delete_book(book_id):
    global books
    books =[book for book in books if book['id'] != int(book_id)]
    return redirect("/home")

@app.route("/book_detail/<book_id>")
def book_details(book_id):
   book = [book for book in books if book["id"] == int(book_id)]
   print(book)
   return render_template('books_details.html' , book = book)
if __name__ == '__main__':
    app.run(debug=True)