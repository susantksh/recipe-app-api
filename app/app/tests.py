"""
sample test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def calc_test(self):
        """Test adding numbers"""
        res = calc.add(5 + 6)

        self.assertEqual(res, 10)

    # def calc_subtract_test(self):
    #     res = calc.subtract(11 - 15)

    #     self.assertEqual(res, 3)