import unittest
from TesterScript import my_func


class TestingScript(unittest.TestCase):
    def test_one(self):
        self.assertEqual(my_func('hello world'), 'Hello World')

    if __name__ == '__main__':
        unittest.main()
