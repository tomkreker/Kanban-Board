import os
import unittest
from app.py import db, app, Task

class Tests(unittest.TestCase):
 
	def setUp(self):
		app.config['TESTING'] = True
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
		self.app = app.test_client()
		db.drop_all()
		db.create_all()
	   
	def test_index(self):
		response = self.app.get('/', follow_redirects=True)
		self.assertEqual(response.status_code, 200)

	def test_add_task(self):
		response = self.app.post(
		  '/form_update',
		  data = dict(text="test", category="To Do"),
		  follow_redirects=True
		)
		self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
	unittest.main()