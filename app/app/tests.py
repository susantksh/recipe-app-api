"""
sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_calc_add(self):
        """Test adding numbers"""
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract_calc(self):
        """testing subtraction"""
        res = calc.subtract(15, 11)

        self.assertEqual(res, 4)
