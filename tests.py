import unittest

from src.beginner_01 import sample_module

class TestClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smoke_test(self):
        assert True == sample_module()
