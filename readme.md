📚 Book Manager Web App
A simple Flask web application that allows users to add, view, and delete books. The application uses in-memory storage and includes basic styling with a custom CSS file.

🚀 Features
View a list of all books.

Add new books with a title, author, and publication year.

View the details of individual books.

Delete books from the list.

Styled with a custom style.css file.

🛠️ Tech Stack
Backend: Python, Flask

Frontend: HTML, CSS, Jinja2

Storage: In-memory list (no database)

📁 Project Structure
Plaintext

.
├── app.py # Main Flask application
├── static/
│ └── style.css # CSS styling file
└── templates/
├── base.html # Base layout template (required)
├── index.html # Homepage: list of books
├── add_book.html # Form to add a new book
└── book_details.html # Book detail page (required)
▶️ How to Run the App
Clone the repository (or download the files):

Bash

git clone <your-repo-url>
cd book-manager
Install dependencies:

Bash

pip install Flask
Run the Flask app:

Bash

python app.py
Open your browser and navigate to:

http://127.0.0.1:5000/home
📌 Available Routes
Route Method Description
/home GET View all books
/add-book GET Form to add a new book
/greet POST Handles submission of a new book
/delete/<book_id> POST Deletes a book by its ID
/book_detail/<book_id> GET Displays details for a specific book

Export to Sheets
🎨 Styling
The static/style.css file contains the custom styles used by the HTML templates. Ensure your base.html template includes a link to this stylesheet:

HTML

<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
📝 Notes
All books are stored in a Python list, meaning data is lost when the server restarts.

You must create base.html and book_details.html for full functionality, as they are referenced in the other templates.

Consider renaming the /greet route to something more descriptive like /add-book (for the POST request) for better clarity.

🧪 Example Book Entry
JSON

{
"id": 3,
"title": "The Hobbit",
"author": "J.R.R. Tolkien",
"year": 1937
}
📄 License
This project is for educational purposes. No license is specified.
