import unittest
import cap_text

class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Python')
    def test_mutiple_word(self):
        text = 'writing python'
        result = cap_text.cap_text(text)
        self.assertEqual(result, 'Writing Python')


if __name__ == '__main__':
    unittest.main()
