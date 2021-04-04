r"""Hello World"""
from flask import Flask, render_template, redirect, request, session, url_for


app = Flask(__name__)
app.secret_key = 'aosfj930fj982f843598h1'


@app.route('/')
def index():
    username = session.get('user_info')
    if username:
        return redirect(url_for('home', username=username))
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'test' \
                and password == 'test':
            session['user_info'] = username
            return redirect(url_for('home', username=username))
        else:
            return render_template('login.html', err="Invalid Username or Password")

    return render_template('login.html')


@app.route('/user/<username>')
def home(username=None):
    if 'user_info' in session \
            and username is session['user_info']:
        return render_template('home.html', username=username)
    else:
        return render_template('home.html')


@app.route('/logout')
def logout():
    del session['user_info']
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
