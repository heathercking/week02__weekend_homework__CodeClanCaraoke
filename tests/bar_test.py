import builtins
import unittest
from unittest import mock
from unittest.mock import patch

from classes.bar import Bar
from classes.room import Room
from classes.guest import Guest
from classes.drink import Drink

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar_1 = Bar("CodeClan Caraoke", 100.00)

        self.room_1 = Room("Muppet Theatre", 5, 100.00)
        self.room_2 = Room("The Stage", 3, 100.00)
        self.room_3 = Room("The Attic", 2, 100.00)

        self.guest_1 = Guest("Kermit the Frog", 32, 20.00, True)
        self.guest_2 = Guest("Miss Piggy", 29, 10.00, False)
        self.guest_3 = Guest("Fozzie the Bear", 40, 15.00, False)
        self.guest_4 = Guest("Beaker", 17, 30.00, False)
        self.guest_5 = Guest("The Swedish Chef", 35, 5.00, False)

        self.drink_1 = Drink("wine", 4.50, 5, 10)
        self.drink_2 = Drink("beer", 3.50, 4, 20)


    def test_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.bar_1.name)
    
    def test_bar_has_tab(self):
        self.assertEqual(0, self.bar_1.bar_tab)
    
    def test_check_guest_is_old_enough_to_buy_alcohol(self):
        self.assertEqual(True, self.bar_1.check_guest_is_old_enough_to_drink(self.guest_1))

    def test_serve_guest_drink__pay_by_tab__True(self):
        input_pay_by_tab = "yes"
        self.bar_1.serve_guest_drink(input_pay_by_tab, self.guest_1, self.drink_1)
        self.assertEqual(4.50, self.guest_1.guest_tab)
        self.assertEqual(20.00, self.guest_1.wallet)

    def test_serve_guest_drink__pay_by_tab__False(self):
        input_pay_by_tab = "no"
        self.bar_1.serve_guest_drink(input_pay_by_tab, self.guest_1, self.drink_1)
        self.assertEqual(0.00, self.guest_1.guest_tab)
        self.assertEqual(15.50, self.guest_1.wallet)

     # def test_add_drink_to_tab_check__True(self, mock_input):
    #     with mock.patch(builtins.input, return_value="yes"):
    #         self.assertEqual(True, self.bar_1.add_drink_to_tab_check(mock_input))

    def test_serve_guest_drink__is_old_enough(self):
        input_pay_by_tab = "no"
        self.bar_1.serve_guest_drink(input_pay_by_tab, self.guest_1, self.drink_1)
        self.assertEqual(15.50, self.guest_1.wallet)

    def test_serve_guest_drink__not_old_enough(self):
        input_pay_by_tab = "no"
        self.bar_1.serve_guest_drink(input_pay_by_tab, self.guest_4, self.drink_1)
        self.assertEqual(30.00, self.guest_4.wallet)
    
    def test_guest_can_pay_tab(self):
        pass
    
    def test_add_new_drink_to_stock(self):
        self.bar_1.add_new_drink_to_stock(self.drink_1)
        self.assertEqual(1, len(self.bar_1.drinks_inventory))

    def test_increase_stock_level_of_a_drink(self):
        self.bar_1.add_new_drink_to_stock(self.drink_1)
        self.bar_1.increase_stock_level_of_a_drink(self.drink_1, 1)
        self.assertEqual(11, self.drink_1.stock_level)
    
    def test_get_total_drinks_stock_level(self):
        self.bar_1.add_new_drink_to_stock(self.drink_1)
        self.bar_1.add_new_drink_to_stock(self.drink_2)
        self.assertEqual(30, self.bar_1.get_total_drinks_stock_level())
    
    def test_get_total_value_of_drinks_stock(self):
        self.bar_1.add_new_drink_to_stock(self.drink_1)
        self.bar_1.add_new_drink_to_stock(self.drink_2)
        self.assertEqual(115.00, self.bar_1.get_total_value_of_drinks_stock())

