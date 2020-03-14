# Kanban-Board
A simple Kanban board application for task management.

## Features

- Add new tasks
- Switch tasks between three categories: To Do, Doing and Done
- Delete tasks (prompting the user for confirmation)
- A lovely dog image to keep you smiling

## Installation

First, download and unzip to get a Kanban-Board directory

Then, create and activate new Python virtual environment (Windows syntax)
```
> python3 -m venv venv 
> \venv\Scripts\activate
```
Install necessary dependencies
```
(venv) > pip3 install -r requirements.txt
```
Define flask app (Windows PowerShell syntax)
```
(venv) > $env:FLASK_APP=app.py
```
Start flask server
```
(venv) > flask run
```
Your Kanban board will now be running at http://127.0.0.1:5000/

## Unit Testing

On the project root directory, run
```
(venv) > python3 unit-tests.py
```
