from pathlib import Path

from flask import Flask, url_for, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Init the flask project.
app = Flask(__name__)
app.config.from_object("configs.DevConfig")