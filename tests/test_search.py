import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSearch(unittest.TestCase):
    def test_partial_title_case_insensitive(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("The Lion King"))

        result = cart.search_by_title("lion")

        self.assertIsNotNone(result)
        self.assertEqual(result.title, "The Lion King")


if __name__ == "__main__":
    unittest.main()