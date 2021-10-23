import unittest
from classes.guest import Guest
from classes.bar import Bar
from classes.room import Room
from classes.song import Song
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Kermit the Frog", 32, 20.00, True)
        self.guest_2 = Guest("Miss Piggy", 29, 10.00, False)
        self.guest_3 = Guest("Fozzie the Bear", 40, 15.00, False)
        self.guest_4 = Guest("Beaker", 17, 30.00, False)
        self.guest_5 = Guest("The Swedish Chef", 35, 5.00, False)

        self.mykaraoke = Bar("CodeClan Caraoke", 100.00)
        self.room_1 = Room("Muppet Theatre", 20, 100.00)
        self.song_2 = Song("Mah Na Mah Na", "Film 1")

        self.drink_1 = Drink("wine", 4.50, 5, 10)
        self.drink_2 = Drink("beer", 3.50, 4, 20)
    
    def test_guest_has_name(self):
        self.assertEqual("Kermit the Frog", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.guest_1.wallet)

    def test_guest_can_pay_entry_fee(self):
        self.guest_1.pay_entry_fee(10.00)
        self.assertEqual(10.00, self.guest_1.wallet)

    def test_favourite_song_reaction(self):
        self.assertEqual("Yaaaas", self.guest_1.favourite_song_reaction())
    
    def test_guest_has_entry_fee_paid_status(self):
        self.assertEqual(True, self.guest_1.entry_fee_paid)
    
    def test_entry_fee_paid_status_updates_when_fee_paid(self):
        entry_fee = 10.00
        self.guest_2.pay_entry_fee(entry_fee)
        self.assertEqual(True, self.guest_2.entry_fee_paid)

    def test_guest_can_buy_drink(self):
        self.guest_1.buy_drink(self.drink_1)
        self.assertEqual(15.50, self.guest_1.wallet)
