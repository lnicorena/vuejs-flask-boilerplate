import unittest
import sys
sys.path.append('../app')
from app import app
import json


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    # Test if application is running
    def test_root_status(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)

    def test_root_content_type(self):
        response = self.app.get('/')
        self.assertIn('application/json', response.content_type)

    def test_root_response(self):
        response = self.app.get('/')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, "It works!")
