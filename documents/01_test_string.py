import unittest

class TestString(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertFalse('foo'.isupper())
        self.assertTrue('FOO'.isupper())

    def test_split(self):
        s = 'good morning'
        self.assertEqual(s.split(' '), ['good', 'morning'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()