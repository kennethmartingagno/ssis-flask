from sqlite3.dbapi2 import connect
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'streetcar'

@app.route('/')
def index():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Students")
    data = cursor.fetchall()
    return render_template("index.html", student=data)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        id_number = request.form['id_number']
        first = request.form['first']
        last = request.form['last']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']

        with sqlite3.connect("students.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Students (id_number, first, last, course, year, gender) values (?,?,?,?,?,?)", (id_number, first, last, course, year, gender))
            conn.commit()
            return redirect(url_for('index'))

@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_student(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Students WHERE id = ?', id)
    data = cursor.fetchall()
    cursor.close()
    return render_template("edit.html", student=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        id_number = request.form['id_number']
        first = request.form['first']
        last = request.form['last']
        course = request.form['course']
        year = request.form['year']
        gender = request.form['gender']

        with sqlite3.connect("students.db") as conn:
            cur = conn.cursor()
            cur.execute("""
            UPDATE Students
            SET id_number = ?,
                first = ?,
                last = ?,
                course = ?,
                year = ?,
                gender = ?
            WHERE id = ?
            """, (id_number, first, last, course, year, gender, id))
            conn.commit()
            return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods=['POST','GET'])
def delete_student(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Students WHERE id = ?', id)
    connection.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)