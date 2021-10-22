import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Kermit the Frog", 32)
        self.guest_2 = Guest("Miss Piggy", 29)
        self.guest_3 = Guest("Fozzie the Bear", 40)
        self.guest_4 = Guest("Beaker", 17)
        self.guest_5 = Guest("The Swedish Chef", 35)