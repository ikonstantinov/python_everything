import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def db_connect():
    return sqlite3.connect('db.sqlite')


def create_table():
    db = db_connect()
    cursor = db.cursor()
    cursor.execute('create table posts(title varchar(100), post varchar(2000))')


@app.route('/')
def index():
    db = db_connect()
    cursor = db.cursor()
    cursor.execute("select title, post from posts")
    
    return render_template('index.html', posts=cursor.fetchall())
   
    
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        db = db_connect()
        cursor = db.cursor()
        cursor.execute(
            'insert into posts (title, post) values (?, ?)',
            (request.form['title'], request.form['post'])
        )
        db.commit()
        return redirect('/')
    return render_template('edit.html')

    
if __name__ == '__main__':
    app.run(debug=True)
