from flask import Flask, render_template, url_for, redirect, request
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="phpmvc"
)

"""-------------HOME---------------"""


@app.route("/")
def index():
    return render_template('home/index.html', menu='home')


"""-------------END HOME---------------"""

"""-------------MAHASISWA---------------"""


@app.route("/mahasiswa")
def mahasiswa():
    query = "SELECT * FROM mahasiswa"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return render_template('mahasiswa/mahasiswa.html', menu='mahasiswa', mhs=result)


@app.route("/mahasiswa/tambah", methods=['GET', 'POST'])
def tambahMahasiswa():
    if request.method == 'POST':
        data = {
            'nama': request.form['nama'],
            'npm': request.form['npm'],
            'email': request.form['email'],
            'jurusan': request.form['jurusan'],
        }

        query = ("INSERT INTO mahasiswa "
                 "(nama, npm, email, jurusan) "
                 "VALUES (%(nama)s, %(npm)s, %(email)s, %(jurusan)s)")
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        return redirect(url_for('mahasiswa'))

    return render_template('/mahasiswa/form.html', menu='mahasiswa', aksi='tambah')


@app.route('/mahasiswa/edit', methods=['GET', 'POST'])
def editMahasiswa():
    id = {'id': request.args.get("id")}

    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'nama': request.form['nama'],
            'npm': request.form['npm'],
            'email': request.form['email'],
            'jurusan': request.form['jurusan'],
        }

        query = ("UPDATE mahasiswa SET nama=%(nama)s, npm=%(npm)s, email=%(email)s, jurusan=%(jurusan)s "
                 "WHERE id=%(id)s")
        cursor = conn.cursor()
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        return redirect(url_for('mahasiswa'))

    query = ("SELECT * FROM mahasiswa "
             "WHERE id=%(id)s")
    cursor = conn.cursor()
    cursor.execute(query, id)
    result = cursor.fetchone()
    cursor.close()
    return render_template('/mahasiswa/form.html', menu='mahasiswa', mhs=result, aksi='edit')


@app.route('/mahasiswa/hapus')
def hapusMahasiswa():
    id = {'id': request.args.get("id")}
    query = ("DELETE FROM mahasiswa "
             "WHERE id=%(id)s")
    cursor = conn.cursor()
    cursor.execute(query, id)
    conn.commit()
    cursor.close()
    return redirect(url_for('mahasiswa'))


@app.route('/mahasiswa/detail')
def detailMahasiswa():
    id = {'id': request.args.get("id")}
    query = ("SELECT * FROM mahasiswa "
             "WHERE id=%(id)s")
    cursor = conn.cursor()
    cursor.execute(query, id)
    result = cursor.fetchone()
    cursor.close()
    return render_template('/mahasiswa/detail.html', menu='mahasiswa', mhs=result)


"""-------------END MAHASISWA---------------"""

"""-------------ABOUT---------------"""


@app.route("/about")
def about():
    return render_template('about/about.html', menu='about')


@app.route('/about/tambah', methods=['GET', 'POST'])
def tambahAbout():
    pass


"""-------------END ABOUT---------------"""

if __name__ == "__main__":
    app.run(debug=True)
