r"""The routing methods."""
from flask import Flask
from routes import *


if __name__ == '__main__':
    app = Flask(__name__)
    app.run()
