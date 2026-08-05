import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    books = get_books()

    return render_template(
        "index.html",
        books=books
    )

def get_books():

    conn = sqlite3.connect("library.db")

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    conn.close()

    return books

if __name__ == "__main__":
    app.run(debug=True)