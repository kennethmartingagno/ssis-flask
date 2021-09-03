from sqlite3.dbapi2 import connect
from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

//comment

app = Flask(__name__)
app.config['SECRET_KEY'] = 'streetcar'

@app.route('/')
def index():
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Students")
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM Courses")
    datas = cursor.fetchall()
    return render_template("index.html", student=data, courses=datas)

@app.route('/search', methods=['GET', 'POST'])
def search_student():
    id_number = request.form.get('id_number')
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Students WHERE id_number = ?", (id_number,))
    data = cursor.fetchall()
    cursor.execute("SELECT * FROM Courses")
    datas = cursor.fetchall()
    return render_template("index.html", student=data, courses=datas)

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

@app.route('/addcourse', methods=['POST'])
def add_course():
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']

        with sqlite3.connect("students.db") as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Courses(course_code, course_name) values (?,?)", (course_code, course_name))
            conn.commit()
            return redirect(url_for('index'))

@app.route('/edit/<id>', methods=['POST', 'GET'])
def get_student(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Students WHERE id = ?', (id,))
    data = cursor.fetchall()
    cursor.close()
    return render_template("edit.html", student=data[0])

@app.route('/edit_course/<id>', methods=['POST', 'GET'])
def edit_course(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Courses WHERE id = ?', (id,))
    data = cursor.fetchall()
    cursor.close()
    return render_template("edit_course.html", courses=data[0])

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

@app.route('/update_course/<id>', methods=['POST'])
def update_course(id):
    if request.method == 'POST':
        course_code = request.form['course_code']
        course_name = request.form['course_name']

        with sqlite3.connect("students.db") as conn:
            cur = conn.cursor()
            cur.execute("""
            UPDATE Courses
            SET course_code = ?,
                course_name = ?
            WHERE id = ?
            """, (course_code, course_name, id))
            conn.commit()
            return redirect(url_for('index'))

@app.route('/delete/<string:id>', methods=['POST','GET'])
def delete_student(id):
    connection = sqlite3.connect("students.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('DELETE FROM Students WHERE id = ?', (id,))
    connection.commit()
    return redirect(url_for('index'))

@app.route('/delete_course/<string:id>', methods=['POST', 'GET'])
def delete_course(id):
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('DELETE FROM Courses WHERE id = ?', (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)