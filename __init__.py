from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def add_student():
    if request.method == "POST":
        id = request.form['id']
        first = request.form['first']
        last = request.form['last']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']
        with sqlite3.connect("students.db") as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO students (id, first, last, course, year, gender) values (?,?,?,?,?,?)", (id, first, last, course, year, gender))
            connection.commit()
        
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)