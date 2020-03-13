from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #maybe need to change place

base_path = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_path, 'database.db')

db = SQLAlchemy(app)

class Task(db.Model):
	__tablename__ = 'Task'
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(100))
	category = db.Column(db.String(10))

db.create_all()
	
@app.route('/')
def index():
	todo = Task.query.filter_by(category='To Do').all()
	doing = Task.query.filter_by(category='Doing').all()
	done = Task.query.filter_by(category='Done').all()
	return render_template('index.html',todo=todo, doing=doing,done=done)

@app.route('/add', methods=['POST'])
def add():
	newtask = Task(text=request.form['newtask'], category=request.form['category'])
	db.session.add(newtask)
	db.session.commit()
	return redirect(url_for('index'))
	
@app.route('/move/<id>/<category>')
def move(id,category):
	task = Task.query.get(id)
	task.category = category
	db.session.commit()
	return redirect(url_for('index'))
	
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
	task = Task.query.get(id)
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)