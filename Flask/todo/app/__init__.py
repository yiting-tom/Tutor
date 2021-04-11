from pathlib import Path

from flask import Flask, url_for, render_template, request, redirect, flash

# Init the flask project.
app = Flask(__name__)
app.config.from_object("configs.DevConfig")
