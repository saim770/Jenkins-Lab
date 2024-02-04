# test_app.py
import unittest
from app import app  # Corrected import for your project structure

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello, this is a secure Flask app!", response.data)

if __name__ == '__main__':
    unittest.main()
