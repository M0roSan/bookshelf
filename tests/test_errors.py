from app import app
import unittest


class TestFlaskBookshel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        #creates a test client
        self.app = app.test_client()
        #propagate the exceptions to the test client'
        self.app.testing = True

    def tearDown(self):
        pass
    
    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        result = self.app.get('/')
        self.assertEqual(result.data, "Hello world!")