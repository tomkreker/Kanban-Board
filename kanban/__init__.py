from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #maybe need to change place

base_path = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_path, 'database.db')

db = SQLAlchemy(app)

from kanban import routes