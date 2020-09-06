
import unittest
from funcs import tashizan, hikizan

class TestKeisan(unittest.TestCase):

    def test_tashizan(self):
        x = 1
        y = 3
        expected = 4
        actual = tashizan(x, y)
        self.assertEqual(expected, actual)

    def test_hikizan(self):
        x = 1
        y = 3
        expected = -2
        actual = hikizan(x, y)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
