import unittest
from classes.bar import Bar
from classes.room import Room
from classes.guest import Guest
from classes.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("wine", 4.50, 5)
        self.drink_2 = Drink("beer", 3.50, 4)

    def test_drink_has_name(self):
        self.assertEqual("wine", self.drink_1.name)

    def test_drink_has_price(self):
        self.assertEqual(4.50, self.drink_1.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(5, self.drink_1.alcohol_level)