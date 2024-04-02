import unittest
from src.multiply import multiply_by_three


class TestMultiplyByThree(unittest.TestCase):

    def test_multiply_by_three(self):
        self.assertEqual(multiply_by_three(3), 9)


unittest.main()
