#!/usr/bin/python3
"""unittest for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """ test for JSON string representation """

        rec1 = Rectangle(6, 4, 5, 9, 59)
        rec_dict = rec1.to_dictionary()
        d1 = '[{"id": 59, "width": 6, "height": 4, "x": 5, "y": 9}]'
        self.assertEqual(d1, Base.to_json_string([rec_dict]))
        self.assertIsInstance(Base.to_json_string([rec_dict]), str)

        s1 = Square(2, 4, 7, 49)
        s_dict = s1.to_dictionary()
        d2 = '[{"id": 49, "size": 2, "x": 4, "y": 7}]'
        self.assertEqual(d2, Base.to_json_string([s_dict]))
        self.assertIsInstance(Base.to_json_string([s_dict]), str)

        self.assertEqual("[]", Base.to_json_string([]))
        self.assertIsInstance(Base.to_json_string([]), str)

    def test_from_json_string(self):
        """test for JSON string to dictionary """

        d3 = '{"id": 59, "width": 6, "height": 4, "x": 5, "y": 9}'
        a_list = Rectangle.from_json_string(d3)
        li1 = {'id': 59, 'width': 6, 'height': 4, 'x': 5, 'y': 9}
        self.assertEqual(li1, a_list)
        self.assertIsInstance(a_list, dict)

        d4 = '{"id": 49, "size": 2, "x": 4, "y": 7}'
        b_list = Square.from_json_string(d4)
        li2 = {'id': 49, 'size': 2, 'x': 4, 'y': 7}
        self.assertEqual(li2, b_list)
        self.assertIsInstance(b_list, dict)


if __name__ == "__main__":
    unittest.main()
