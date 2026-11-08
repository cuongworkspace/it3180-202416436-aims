import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_cart_limit(self):
        cart = Cart()
        for i in range(20):
            self.assertTrue(
                cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=10))
            )
        self.assertFalse(
            cart.add_dvd(DigitalVideoDisc("DVD 21", cost=10))
        )