import os
import unittest
from kanban import db, app

class Tests(unittest.TestCase):
 
	def setUp(self):
	''' Set up the test settings as appropriate for Flask'''
		app.config['TESTING'] = True
		app.config['DEBUG'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///unit_tests.db'
		self.app = app.test_client()
		db.create_all()
		
		self.assertEqual(app.debug, False)
		
	def tearDown(self):
	'''Clean the db after each test'''
		db.session.remove()
		db.drop_all()
	   
	def test_index(self):
	'''Test the that main page is retrieved on default'''
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_add_task(self):
		'''Test adding tasks - using the add POST method and retrieving HTTP 200'''
		response = self.app.post(
		  '/add',
		  data = dict(text="test", category="To Do"),
		  follow_redirects=True
		)
		self.assertEqual(response.status_code, 200) #maybe also that the task is in db
		
	def test_move_task(self):
		'''Test moving tasks - using the add GET method used by the moving links and retrieving HTTP 200'''
		self.test_add_task() #create a new task to move
		movements = ['Doing','Done','Doing','To Do'] #Test all possible movements To DO->Done and back
		for move in movements:
			response = self.app.get('/move/1/'+move, follow_redirects=True) #a simplification - using 1 as id
			self.assertEqual(response.status_code, 200)
			
	def test_delete_task(self):
		self.test_add_task() #create a new task to delete
		response = self.app.post(
		  '/delete/1',
		  data = dict(id=1),
		  follow_redirects=True
		)
		self.assertEqual(response.status_code, 200) #maybe also that task is NA

if __name__ == "__main__":
	unittest.main()