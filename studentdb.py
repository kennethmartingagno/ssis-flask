import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

connection.execute("""CREATE TABLE students (
                        id TEXT PRIMARY KEY,
                        first TEXT NOT NULL,
                        last TEXT NOT NULL,
                        course TEXT NOT NULL,
                        year TEXT NOT NULL,
                        gender TEXT NOT NULL    
                    )""")

connection.commit()

connection.close()