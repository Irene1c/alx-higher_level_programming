#!/usr/bin/python3
"""unittest for the Base class"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """a class to test base"""

    def test_id(self):
        """ testing the value of id"""

        b1 = Base()
        b2 = Base(4)
        b3 = Base(9)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 2)
