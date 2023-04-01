import unittest
from utils.dicts import get_val

class TestArrs(unittest.TestCase):
    def test_get_val(self):
        data = {"10+10": "equal 20", "11+11": "equal 20 (twenty too)"}
        self.assertEqual(get_val(data, "10+10", "true"), "equal 20")
        self.assertEqual(get_val(data, "11+11", "joke"), "equal 20 (twenty too)")
        self.assertEqual(get_val({}, "10+10", "def"), "def")
        self.assertEqual(get_val(data, "10+10"), "equal 20")
