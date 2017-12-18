from flask import Flask, render_template, request, redirect, g, session
import redis

app = Flask(__name__)

@app.before_request
def before():
    g.r = redis.StrictRedis()

@app.route('/')
def index():
    links = [link.decode('utf-8') for link in g.r.lrange('bookmarks', 0, -1)]
    return render_template(
        'index.html',
        links=links,
        message=session.pop('message', '')
    )

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        if request.form['link']:
            g.r.lpush('bookmarks', request.form['link'])
            session['message'] = 'Link successfully added'
            return redirect('/')
    return render_template('add.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app.run(debug=True)
