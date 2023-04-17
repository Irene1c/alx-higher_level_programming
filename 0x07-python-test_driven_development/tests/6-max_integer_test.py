#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ A class that tests for max_integer """

    def test_max_integer(self):
        """ testing for max integer at various locations """

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([41, 32, 23, 14]), 41)
        self.assertEqual(max_integer([12, 25, 96, 78, 5, 70]), 96)

    def test_empty_list(self):
        """ test for empty list """

        self.assertIsNone(max_integer([]))

    def test_argument_list(self):
        """ test for one argument list """

        self.assertEqual(max_integer([3]), 3)

if __name__ == "__main__":
    unittest.main()
