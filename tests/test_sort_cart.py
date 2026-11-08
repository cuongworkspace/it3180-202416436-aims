import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSortCart(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()
        self.cart.add_dvd(DigitalVideoDisc("Zebra", cost=30))
        self.cart.add_dvd(DigitalVideoDisc("Apple", cost=50))
        self.cart.add_dvd(DigitalVideoDisc("Banana", cost=10))

    def test_sort_by_title(self):
        self.cart.sort_by_title()
        titles = [dvd.title for dvd in self.cart.items]
        self.assertEqual(titles, ["Apple", "Banana", "Zebra"])

    def test_sort_by_cost(self):
        self.cart.sort_by_cost()
        costs = [dvd.cost for dvd in self.cart.items]
        self.assertEqual(costs, [10, 30, 50])


if __name__ == "__main__":
    unittest.main()
    