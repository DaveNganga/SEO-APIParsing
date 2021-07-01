import unittest
from StyleuineaPig import prime_factors


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(prime_factors(5), 5)

if __name__ == '__main__':
    unittest.main()
