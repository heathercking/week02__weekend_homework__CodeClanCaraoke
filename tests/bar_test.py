import unittest
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


    def test_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.bar_1.name)
    
    def test_bar_has_tab(self):
        self.assertEqual(0, self.bar_1.bar_tab)

        


