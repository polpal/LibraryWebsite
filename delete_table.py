import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS books")

conn.commit()
conn.close()

print("Table deleted successfully.")