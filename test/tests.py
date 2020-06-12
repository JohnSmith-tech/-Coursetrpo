import unittest
from src.program import error
from src.program import checking

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

    def test_check1(self):
        ch_1 = checking('drive12r', ['водитель', 'driver'])
        self.assertEqual(False, ch_1)

    def test_check2(self):
        ch_2 = checking('', ['водитель', 'driver'])
        self.assertEqual(False, ch_2)

    def test_check3(self):
        ch_3 = checking(' ', ['полицейский', 'police'])
        self.assertEqual(False, ch_3)

    def test_check4(self):
        ch_4 = checking(' police', ['полицейский', 'police'])
        self.assertEqual(False, ch_4)

    def test_check5(self):
        ch_5 = checking('driver', ['водитель', 'driver'])
        self.assertEqual(True, ch_5)

    def test_check6(self):
        ch_6 = checking('police', ['полицейский', 'police'])
        self.assertEqual(True, ch_6)

if __name__ == '__main__':
    unittest.main()


