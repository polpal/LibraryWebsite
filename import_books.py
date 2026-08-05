import sqlite3
import pandas as pd

# Read Excel
df = pd.read_excel("data/library.xlsx")

# Connect to SQLite
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Optional: Remove existing data before importing
cursor.execute("DELETE FROM books")

# Import each row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO books
        (accession_no, title, author, category, status)
        VALUES (?, ?, ?, ?, ?)
    """, (
        str(row["পুস্তকের নং"]),
        str(row["পুস্তকের নাম"]),
        str(row["লেখকের নাম"]),
        str(row["বিষয়"]),
        "Available"
    ))

conn.commit()
conn.close()

print("Books imported successfully!")