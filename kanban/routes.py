from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from kanban import db, app

class Task(db.Model): #A Task table 
	__tablename__ = 'Task'
	id = db.Column(db.Integer, primary_key=True) #a unique identifier for each task
	text = db.Column(db.String(100)) #the description of the task
	category = db.Column(db.String(10)) #to do / doing / done

db.create_all() #create the tables
	
@app.route('/')
def index():
	'''Fetch all tasks from the three categories and pass to index.html'''
	todo = Task.query.filter_by(category='To Do').all()
	doing = Task.query.filter_by(category='Doing').all()
	done = Task.query.filter_by(category='Done').all()
	return render_template('index.html',todo=todo, doing=doing,done=done)

@app.route('/add', methods=['POST'])
def add():
	'''Fetch get a new task from the form, add it to the db, return to index page'''
	newtask = Task(text=request.form['text'], category=request.form['category'])
	db.session.add(newtask)
	db.session.commit()
	return redirect(url_for('index'))
	
@app.route('/move/<id>/<category>')
def move(id,category):
	'''Move the chosen task to a new category based on the clicked button'''
	task = Task.query.get(id)
	task.category = category #this is given by which button was pressed on the page
	db.session.commit()
	return redirect(url_for('index'))
	
@app.route('/delete/<id>', methods=['POST'])
def delete(id):
	'''Delete a given task from the db and return the index page'''
	task = Task.query.get(id)
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)