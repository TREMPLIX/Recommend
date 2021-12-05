import unittest
from calc import calculation


class CalcTest(unittest.TestCase):
    def test_add(self):
        self.cl = calculation()
        a = 2
        b = 3
        true_value = 5
        test_value = self.cl.add(a, b)
        self.assertEqual(true_value, test_value)

    def test_sub(self):
        self.cl = calculation()
        a = 5
        b = 6
        true_value = -1
        test_value = self.cl.sub(a, b)
        self.assertEqual(true_value, test_value)


if __name__ == '__main__':
    unittest.main()
