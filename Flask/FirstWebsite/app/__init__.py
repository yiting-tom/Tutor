import os
from pathlib import Path

from flask import url_for, render_template, Flask, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

# Initialize the flask object.

app = Flask(__name__)
root_path = Path(__file__).cwd()

app.config['SLQALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + str(root_path / "data.sqlite")
db = SQLAlchemy(app)
