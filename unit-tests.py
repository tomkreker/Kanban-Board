import os
import unittest
from kanban import db, app

class Tests(unittest.TestCase):
 
	def setUp(self):
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unit_tests.db'
		self.app = app.test_client()
		db.create_all()
		
		self.assertEqual(app.debug, False)
		
	def tearDown(self):
		db.session.remove()
		db.drop_all()
	   
	def test_index(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_add_task(self):
		response = self.app.post(
		  '/add',
		  data = dict(text="test", category="To Do"),
		  follow_redirects=True
		)
		self.assertEqual(response.status_code, 200) #maybe also that the task is in db
		
	def test_move_task(self):	
		self.test_add_task()
		movements = ['Doing','Done','Doing','To Do']
		for move in movements:
			response = self.app.get('/move/1/'+move, follow_redirects=True)
			self.assertEqual(response.status_code, 200)
			
	def test_delete_task(self):
		self.test_add_task()
		response = self.app.post(
		  '/delete/1',
		  data = dict(id=1),
		  follow_redirects=True
		)
		self.assertEqual(response.status_code, 200) #maybe also that task is NA

if __name__ == "__main__":
	unittest.main()