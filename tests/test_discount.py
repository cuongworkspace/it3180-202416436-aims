import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestDiscount(unittest.TestCase):

    def test_discount_20_percent(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("Test", cost=100))
        self.assertEqual(cart.discounted_total(20), 80)

    def test_invalid_discount(self):
        cart = Cart()
        with self.assertRaises(ValueError):
            cart.discounted_total(150)


if __name__ == "__main__":
    unittest.main()