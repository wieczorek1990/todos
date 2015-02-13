import main
import unittest

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()

    def test_hello_world(self):
        message = self.app.get('/')
        assert message.data == 'Hello World!'

if __name__ == '__main__':
    unittest.main()
