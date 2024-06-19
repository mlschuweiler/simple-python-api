import unittest
from src.example import main_function

class TestExample(unittest.TestCase):
    def setUp(self):
        self._test = "test"
    
    def tearDown(self):
        del self

    def test_example_use_case(self):
        self.assertTrue(self._test == "test")
    
    def test_main_function(self):
        expected = "Hello World!"
        actual = main_function()
        self.assertEqual(expected, actual)
