import sqlite3


connection = sqlite3.connect("library.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS books (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    accession_no TEXT,

    title TEXT,

    book_name TEXT,

    author TEXT,

    category TEXT,

    status TEXT

)
""")


connection.commit()

connection.close()


print("Library database created successfully!")