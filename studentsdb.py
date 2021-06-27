import sqlite3

conn = sqlite3.connect("students.db")

cur = conn.cursor()

conn.execute("""CREATE TABLE Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_number TEXT,
    first TEXT,
    last TEXT,
    course TEXT,
    year TEXT,
    gender TEXT
)""")

conn.execute("""CREATE TABLE Courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_code TEXT,
    course_name TEXT
)""")

conn.close()