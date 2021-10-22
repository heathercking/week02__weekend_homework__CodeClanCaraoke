import unittest
from classes.guest import Guest
from classes.karaoke_bar import Karaoke_Bar

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Kermit the Frog", 32, 20.00)
        self.guest_2 = Guest("Miss Piggy", 29, 10.00)
        self.guest_3 = Guest("Fozzie the Bear", 40, 15.00)
        self.guest_4 = Guest("Beaker", 17, 30.00)
        self.guest_5 = Guest("The Swedish Chef", 35, 5.00)

        self.mykaraoke = Karaoke_Bar("CodeClan Caraoke")
    
    def test_guest_has_name(self):
        self.assertEqual("Kermit the Frog", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(32, self.guest_1.age)

    def test_guest_has_wallet(self):
        self.assertEqual(20.00, self.guest_1.wallet)

    def test_guest_can_pay_entry_fee__sufficient_funds(self):
        self.guest_1.pay_entry_fee(10.00)
        self.assertEqual(10.00, self.guest_1.wallet)

    def test_guest_can_pay_entry_fee__insufficient_funds(self):
        self.guest_5.pay_entry_fee(10.00)
        self.assertEqual(5.00, self.guest_5.wallet)

    def test_guest_has_sufficient_funds__True(self):
        entry_fee = 10.00
        self.assertEqual(True, self.guest_1.check_sufficient_funds(entry_fee))

    def test_guest_has_sufficient_funds__False(self):
        entry_fee = 10.00
        self.assertEqual(False, self.guest_5.check_sufficient_funds(entry_fee))