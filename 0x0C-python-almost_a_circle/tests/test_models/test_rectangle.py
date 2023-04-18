#!/usr/bin/python3
"""unittest for the Rectangle class"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """a class to test rectangle"""

    def test_automatic_id(self):
        """ testing assigning id automatically"""

        r1 = Rectangle(1, 2)
        r2 = Rectangle(6, 9, 7)
        r3 = Rectangle(6, 2, 9, 6)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_id(self):
        """ testing the value of id"""

        r4 = Rectangle(4, 6, 0, 4, 9)
        r5 = Rectangle(3, 7, 5, 0, 6)
        self.assertEqual(r4.id, 9)
        self.assertEqual(r5.id, 6)

    def test_one_arg(self):
        """ testing for one argument passed """

        self.assertRaises(TypeError, Rectangle, (9))

    def test_no_arg(self):
        """ testing for no argument passed """

        self.assertRaises(TypeError, Rectangle, ())

    def test_type_width(self):
        """ validating type of width value """

        rect1 = Rectangle(4, 9)
        self.assertIsInstance(4, int)

        self.assertRaises(TypeError, Rectangle, ("3", 2))
        self.assertRaises(TypeError, Rectangle, ([3, 4], 2))
        self.assertRaises(TypeError, Rectangle, ((5, 3), 2))
        self.assertRaises(TypeError, Rectangle, ({4, 6}, 2))
        self.assertRaises(TypeError, Rectangle, (True, 2))

    def test_type_height(self):
        """ validating type of height value """

        rect2 = Rectangle(4, 9)
        self.assertIsInstance(9, int)

        self.assertRaises(TypeError, Rectangle, (3, "2"))
        self.assertRaises(TypeError, Rectangle, (3, [3, 7]))
        self.assertRaises(TypeError, Rectangle, (3, (5, 8)))
        self.assertRaises(TypeError, Rectangle, (3, {9, 6}))
        self.assertRaises(TypeError, Rectangle, (3, False))

    def test_type_x(self):
        """ validating type of the x value """

        rect3 = Rectangle(4, 9, 12, 6)
        self.assertIsInstance(12, int)

        self.assertRaises(TypeError, Rectangle, (3, 2, "6", 2))
        self.assertRaises(TypeError, Rectangle, (3, 2, [3, 5], 2))
        self.assertRaises(TypeError, Rectangle, (3, 2, (2, 7), 2))
        self.assertRaises(TypeError, Rectangle, (3, 2, {2, 8}, 2))
        self.assertRaises(TypeError, Rectangle, (3, 2, True, 2))

    def test_type_y(self):
        """ validating type of the y value """

        rect4 = Rectangle(4, 9, 12, 6)
        self.assertIsInstance(6, int)

        self.assertRaises(TypeError, Rectangle, (3, 2, 6, "9"))
        self.assertRaises(TypeError, Rectangle, (3, 2, 6, [6, 7]))
        self.assertRaises(TypeError, Rectangle, (3, 2, 6, (4, 1)))
        self.assertRaises(TypeError, Rectangle, (3, 2, 6, {9, 4}))
        self.assertRaises(TypeError, Rectangle, (3, 2, 6, False))

    def test_value_attributes(self):
        """ Validating the value of attributes if > 0 """

        rect5 = Rectangle(4, 9, 12, 6)
        self.assertGreater(4, 0)
        self.assertGreater(9, 0)
        self.assertGreater(12, 0)
        self.assertGreater(6, 0)

        with self.assertRaises(ValueError):
            Rectangle(-6, 2)

        with self.assertRaises(ValueError):
            Rectangle(3, -2)

        with self.assertRaises(ValueError):
            Rectangle(3, 2, -9, 4)

        with self.assertRaises(ValueError):
            Rectangle(7, 5, 3, -2)

    def test_area(self):
        """ testing the area of the rectangle """

        rect6 = Rectangle(5, 7, 6, 8, 2)
        self.assertEqual(rect6.area(), 35)

    def test_display(self):
        """ testing display of a rectangle instance """

        pass

    def test_str(self):
        """ Test printable string representation of an instance """

        rect8 = Rectangle(5, 1, 9, 6, 52)
        self.assertEqual(rect8.__str__(), "[Rectangle] (52) 9/6 - 5/1")

    def test_update_args(self):
        """ test for updating attribute values with args (non-keyworded)"""

        rect9 = Rectangle(19, 15, 12, 1, 22)
        self.assertEqual(rect9.__str__(), "[Rectangle] (22) 12/1 - 19/15")

        rect9.update(49)
        self.assertEqual(rect9.__str__(), "[Rectangle] (49) 12/1 - 19/15")

        rect9.update(49, 4)
        self.assertEqual(rect9.__str__(), "[Rectangle] (49) 12/1 - 4/15")

        rect9.update(49, 4, 2)
        self.assertEqual(rect9.__str__(), "[Rectangle] (49) 12/1 - 4/2")

        rect9.update(49, 4, 2, 5)
        self.assertEqual(rect9.__str__(), "[Rectangle] (49) 5/1 - 4/2")

        rect9.update(49, 4, 2, 5, 3)
        self.assertEqual(rect9.__str__(), "[Rectangle] (49) 5/3 - 4/2")

    def test_update_kwargs(self):
        """ test for updating attribute values with kwargs (keyworded)"""

        rect10 = Rectangle(1, 2, 3, 4, 90)
        self.assertEqual(rect10.__str__(), "[Rectangle] (90) 3/4 - 1/2")

        rect10.update(id=89)
        self.assertEqual(rect10.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        rect10.update(width=7, height=2)
        self.assertEqual(rect10.__str__(), "[Rectangle] (89) 3/4 - 7/2")

        rect10.update(width=2, height=5, x=3)
        self.assertEqual(rect10.__str__(), "[Rectangle] (89) 3/4 - 2/5")

        rect10.update(width=4, height=2, x=1, y=7, id=69)
        self.assertEqual(rect10.__str__(), "[Rectangle] (69) 1/7 - 4/2")

    def test_to_dict(self):
        """ test for dictionary representation of Rectangle instance """

        rect11 = Rectangle(1, 2, 3, 4, 77)
        self.assertEqual(rect11.__str__(), "[Rectangle] (77) 3/4 - 1/2")
        a_dict = {'id': 77, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rect11.to_dictionary(), a_dict)


if __name__ == "__main__":
    unittest.main()
