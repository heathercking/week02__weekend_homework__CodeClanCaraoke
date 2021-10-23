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

        self.drink_1 = Drink("wine", 4.50, 5)
        self.drink_2 = Drink("beer", 3.50, 4)


    def test_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.bar_1.name)
    
    def test_bar_has_tab(self):
        self.assertEqual(0, self.bar_1.bar_tab)
    
    def test_check_guest_is_old_enough_to_buy_alcohol(self):
        self.assertEqual(True, self.bar_1.check_guest_is_old_enough_to_drink(self.guest_1))

    #TESTS PASS BUT ARE AFFECTED BY USER INPUT IN TAB CHECK-- HOW TO SOLVE??
    # def test_serve_guest_drink__is_old_enough(self):
    #     self.bar_1.serve_guest_drink(self.guest_1, self.drink_1)
    #     self.assertEqual(15.50, self.guest_1.wallet)

    # def test_serve_guest_drink__not_old_enough(self):
    #     self.bar_1.serve_guest_drink(self.guest_4, self.drink_1)
    #     self.assertEqual(30.00, self.guest_4.wallet)

    
    def test_add_drink_to_tab_check__True(self, mock_input):
        with mock.patch(builtins.input, return_value="yes"):
            self.assertEqual(True, self.bar_1.add_drink_to_tab_check(mock_input))
    
    # def test_add_drink_to_tab_check__False(self):
    #     self.assertEqual(False, self.bar_1.add_drink_to_tab_check())

    # def test_serve_guest_drink__add_to_guest_tab(self):
    #     self.bar_1.serve_guest_drink(self.guest_1, self.drink_1)
    #     self.assertEqual(4.50, self.guest_1.guest_tab)

