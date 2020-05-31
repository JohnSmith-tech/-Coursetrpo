import unittest
from program import error

class TestUnits(unittest.TestCase):
    def test_blocked_1(self):
        bl_1 = error('poLICE')
        self.assertEqual(False, bl_1)

    def test_blocked_2(self):
        bl_2 = error('police')
        self.assertEqual(True, bl_2)
    def test_blocked_3(self):
        bl_3 = error('pol1ce')
        self.assertEqual(False, bl_3)

    def test_blocked_4(self):
        bl_4 = error(' police')
        self.assertEqual(False, bl_4)

    def test_blocked_5(self):
        bl_5 = error('213112')
        self.assertEqual(False, bl_5)


if __name__ == '__main__':
    unittest.main()

