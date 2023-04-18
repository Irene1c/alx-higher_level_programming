#!/usr/bin/python3
"""unittest for the Square class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """a class to test Square instance """

    def test_automatic_id(self):
        """ testing assigning id automatically"""

        s1 = Square(1, 2)
        s2 = Square(6, 9, 7)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_id(self):
        """ testing the value of id"""

        s3 = Square(4, 6, 4, 9)
        s4 = Square(3, 7, 5, 6)
        self.assertEqual(s3.id, 9)
        self.assertEqual(s4.id, 6)

    def test_no_arg(self):
        """ testing for no argument passed """

        self.assertRaises(TypeError, Square, ())

    def test_more_args(self):
        """ testing for out of range arguments passed """

        self.assertRaises(TypeError, Square, (1, 2, 5, 90, 7, 3))

    def test_type_size(self):
        """ validating type of width value """

        sq1 = Square(9)
        self.assertIsInstance(9, int)

        self.assertRaises(TypeError, Square, ("3"))
        self.assertRaises(TypeError, Square, ([3, 4]))
        self.assertRaises(TypeError, Square, ((5, 3)))
        self.assertRaises(TypeError, Square, ({4, 6}))
        self.assertRaises(TypeError, Square, (True))

    def test_type_x(self):
        """ validating type of the x value """

        sq3 = Square(4, 9, 16)
        self.assertIsInstance(9, int)

        self.assertRaises(TypeError, Square, (3, "6", 12))
        self.assertRaises(TypeError, Square, (3, [3, 5], 4))
        self.assertRaises(TypeError, Square, (3, (2, 7), 1))
        self.assertRaises(TypeError, Square, (3, {2, 8}, 2))
        self.assertRaises(TypeError, Square, (3, True, 7))

    def test_type_y(self):
        """ validating type of the y value """

        sq4 = Square(4, 9, 5)
        self.assertIsInstance(5, int)

        self.assertRaises(TypeError, Square, (3, 2, "9"))
        self.assertRaises(TypeError, Square, (4, 2, [6, 7]))
        self.assertRaises(TypeError, Square, (7, 2, (4, 1)))
        self.assertRaises(TypeError, Square, (3, 6, {9, 4}))
        self.assertRaises(TypeError, Square, (2, 6, False))

    def test_value_attributes(self):
        """ Validating the value of Square attributes if > 0 """

        sq5 = Square(4, 12, 6)
        self.assertGreater(4, 0)
        self.assertGreater(12, 0)
        self.assertGreater(6, 0)

        with self.assertRaises(ValueError):
            Square(-6)

        with self.assertRaises(ValueError):
            Square(0)

        with self.assertRaises(ValueError):
            Square(2, -9, 4)

        with self.assertRaises(ValueError):
            Square(5, 3, -2)

    def test_str(self):
        """ Test printable string representation of square instance """

        sq6 = Square(5, 9, 6, 58)
        self.assertEqual(sq6.__str__(), "[Square] (58) 9/6 - 5")

    def test_area(self):
        """ testing the area of a Square instance """

        sq7 = Square(7, 6, 8, 65)
        self.assertEqual(sq7.area(), 49)

    def test_display(self):
        """ testing display of a Square instance """

        pass

    def test_update_args(self):
        """ test for updating attribute values with args (non-keyworded)"""

        sq9 = Square(19, 12, 1, 22)
        self.assertEqual(sq9.__str__(), "[Square] (22) 12/1 - 19")

        sq9.update(49)
        self.assertEqual(sq9.__str__(), "[Square] (49) 12/1 - 19")

        sq9.update(49, 4)
        self.assertEqual(sq9.__str__(), "[Square] (49) 12/1 - 4")

        sq9.update(49, 4, 5)
        self.assertEqual(sq9.__str__(), "[Square] (49) 5/1 - 4")

        sq9.update(49, 4, 5, 3)
        self.assertEqual(sq9.__str__(), "[Square] (49) 5/3 - 4")

    def test_update_kwargs(self):
        """ test for updating attribute values with kwargs (keyworded)"""

        sq10 = Square(1, 3, 4, 90)
        self.assertEqual(sq10.__str__(), "[Square] (90) 3/4 - 1")

        sq10.update(id=89)
        self.assertEqual(sq10.__str__(), "[Square] (89) 3/4 - 1")

        sq10.update(size=7)
        self.assertEqual(sq10.__str__(), "[Square] (89) 3/4 - 7")

        sq10.update(size=2, x=3)
        self.assertEqual(sq10.__str__(), "[Square] (89) 3/4 - 2")

        sq10.update(size=4, x=1, y=7, id=69)
        self.assertEqual(sq10.__str__(), "[Square] (69) 1/7 - 4")

    def test_to_dict(self):
        """ test for dictionary representation of Square instance """

        sq11 = Square(9, 3, 4, 77)
        self.assertEqual(sq11.__str__(), "[Square] (77) 3/4 - 9")
        a_dict = {'id': 77, 'size': 9, 'x': 3, 'y': 4}
        self.assertEqual(sq11.to_dictionary(), a_dict)


if __name__ == "__main__":
    unittest.main()
