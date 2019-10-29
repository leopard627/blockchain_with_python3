import unittest

from src.beginner_01 import sample_module, add_value, get_status

class TestClass(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_smoke_test(self):
        assert True == sample_module()

    def test_block_chain_return_value_test(self):
        add_value(10)
        add_value(10, 20)
        add_value(20, 30)
        get_status()
