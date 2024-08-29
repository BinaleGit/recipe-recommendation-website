import unittest
from app import app

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome to the Recipe Recommendation API!', result.data)

    def test_add_recipe(self):
        result = self.app.get('/add-test-recipe')
        self.assertEqual(result.status_code, 201)
        self.assertIn(b'Test recipe added successfully!', result.data)

if __name__ == '__main__':
    unittest.main()
