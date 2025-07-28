# 📚 Book Manager Web App

A simple Flask web application that allows users to add, view, and delete books. The application uses in-memory storage and includes basic styling with a custom CSS file.

---

## 🚀 Features

- View a list of books
- Add new books with title, author, and publication year
- View details of individual books
- Delete books from the list
- Styled with a custom `style.css`

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, Jinja2 templates
- **Storage:** In-memory list (no database)

---

## 📁 Project Structure

```
.
├── app.py                     # Main Flask application
├── static/
│   └── style.css              # CSS styling file
├── templates/
│   ├── base.html              # Base layout template (required)
│   ├── index.html             # Homepage: list of books
│   ├── add_book.html          # Form to add a new book
│   └── books_details.html     # Book detail page (required)
```

---

## ▶️ How to Run the App

1. **Clone the repository** (or download the files):

   ```bash
   git clone <repo-url>
   cd book-manager
   ```

2. **Install dependencies**:

   ```bash
   pip install Flask
   ```

3. **Run the Flask app**:

   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/home
   ```

---

## 📌 Available Routes

| Route                    | Method | Description                          |
| ------------------------ | ------ | ------------------------------------ |
| `/home`                  | GET    | View all books                       |
| `/add-book`              | GET    | Form to add a new book               |
| `/greet`                 | POST   | Handles submission of new book       |
| `/delete/<book_id>`      | POST   | Deletes a book by its ID             |
| `/book_detail/<book_id>` | GET    | Displays details for a specific book |

---

## 🎨 Styling

The `static/style.css` file contains the custom styles used by the HTML templates. Ensure your `base.html` template includes a link to this stylesheet:

```html
<link
  rel="stylesheet"
  href="{{ url_for('static', filename='style.css') }}" />
```

---

## 📝 Notes

- All books are stored in a Python list, meaning data is lost when the server restarts.
- You must create `base.html` and `books_details.html` for full functionality (they are referenced in the templates).
- Consider renaming the route `/greet` to something more descriptive like `/add-book` for clarity.

---

## 🧪 Example Book Entry

```json
{
  "id": 3,
  "title": "The Hobbit",
  "author": "J.R.R. Tolkien",
  "year": 1937
}
```

---

## 📄 License

This project is for educational purposes. No license specified.
