from flask import Flask, render_template, request, redirect, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'SomeKey'


@app.before_request
def before_request():
    g.db = sqlite3.connect('blog.sqlite3')
    g.message = session.pop('message', '')



@app.after_request
def after_request(response):
    g.db.close()
    return response


@app.route('/')
def index():
    cursor = g.db.execute("SELECT * from posts ORDER BY ID DESC")
    posts = cursor.fetchall()
    session['message'] = 'Post Added'
    return render_template('index.html', posts=posts, message=g.message)


@app.route('/add', methods=['GET', 'POST'])
def add():
    name = post = ''
    if request.method == 'POST':
        post = request.form.get('post', '')
        name = request.form.get('name', '')
        if post and name:
            print('Congrats!')
            g.db.execute("INSERT INTO posts (name, post) VALUES (?, ?)", (name, post))
            g.db.commit()
            g.db.close()
            session['message'] = 'Post has been added successfully!'
            return redirect('/')
        return render_template('add.html', name=name, post=post)

    else:
        return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)