from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
r"""5 main Options
    @app.route('/.../<CONVERTER:...>, )
    @app.route('/user/<username>', )
    @app.route('/post/<int:post_id>', )
    @app.route('/post/<float:post_id>', )
    @app.route('/post/<path:path>', )
    @app.route('/login', methods=['GET', 'POST'])
"""


@app.route(rule='/route_1',
           methods=['GET', 'POST'],     # Request methods.
           endpoint='r1',               # Route name.
           defaults={'db': 'test_db'},  # Default params for function.
           redirect_to='/route_2')     # Redirect original url to another.
def route_1(db: str):
    r"""Method 1. using decorator."""
    # do some db things.
    return 'route_1'


def route_2():
    r"""Method 2. using add_url_rule function."""
    return 'route_2'
app.add_url_rule(rule='/route_2', view_func=route_2, endpoint='r2')
