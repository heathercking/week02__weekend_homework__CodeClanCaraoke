import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

import pdb

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Muppet Theatre", 20, 100.00)
        self.room_2 = Room("The Stage", 15, 100.00)
        self.room_3 = Room("The Attic", 2, 100.00)

        self.guest_1 = Guest("Kermit the Frog", 32, 20.00, True)
        self.guest_2 = Guest("Miss Piggy", 29, 10.00, True)
        self.guest_3 = Guest("Fozzie the Bear", 40, 15.00, True)
        self.guest_4 = Guest("Beaker", 17, 30.00, False)
        self.guest_5 = Guest("The Swedish Chef", 35, 5.00, False)

        self.song_1 = Song("The Muppet Show Theme")
        self.song_2 = Song("Mah Na Mah Na")
        self.song_3 = Song("Together Again")
        self.song_4 = Song("Happiness Hotel")
        self.song_5 = Song("It's Not Easy Being Green")


    def test_room_has_name(self):
        self.assertEqual("Muppet Theatre", self.room_1.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(20, self.room_1.max_capacity)
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    # def test_add_multiple_guests_to_room(self):
    #     guests_to_add = [self.guest_1, self.guest_2]
    #     self.room_1.add_guest_to_room(guests_to_add)
    #     self.assertEqual(2, len(self.room_1.guest_list))

    def test_add_guest_to_room__free_spaces_decrease(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(19, self.room_1.free_spaces)

    def test_add_guest_to_room__not_enough_space(self):
        self.room_3.add_guest_to_room(self.guest_1)
        self.room_3.add_guest_to_room(self.guest_2)
        self.room_3.add_guest_to_room(self.guest_3)
        self.assertEqual(2, len(self.room_3.guest_list))
    
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
    
    def test_remove_guest_from_room__free_spaces_increase(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_3)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(18, self.room_1.free_spaces)

    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))
    
    def test_remove_song_from_room(self):
        self.room_1.add_song_to_room(self.song_1)  
        self.room_1.add_song_to_room(self.song_2)      
        self.room_1.remove_song_from_room(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))

    def test_check_room_has_capacity_for_all_guests__True(self):
        self.assertEqual(True, self.room_1.check_room_has_capactiy(20))
    
    def test_check_room_has_capacity_for_all_guests__False(self):
        self.assertEqual(False, self.room_1.check_room_has_capactiy(25))

    def test_view_room_song_list__contains_favourite_song(self):
        self.room_1.add_song_to_room(self.song_1)  
        self.room_1.add_song_to_room(self.song_2)
        self.room_1.add_song_to_room(self.song_3) 
        self.room_1.view_room_song_list()

    def test_favourite_song_check__favourite_song_in_list(self):
        self.room_1.add_song_to_room(self.song_1)  
        self.room_1.add_song_to_room(self.song_2)
        self.room_1.add_song_to_room(self.song_3) 
        self.assertEqual("Yaaaas", self.room_1.favourite_song_check(self.song_2))
    
    # def test_favourite_song_check__favourite_song_not_in_list(self):
    #     self.room_1.add_song_to_room(self.song_1.name)  
    #     self.room_1.add_song_to_room(self.song_3.name) 
    #     self.assertEqual("Add it!", self.room_1.favourite_song_check(self.song_2.name))

    def test_room_has_till(self):
        self.assertEqual(100.00, self.room_1.till)
    
    def test_collect_entry_fee__customer_sufficient_funds(self):
        entry_fee = 10.00
        self.room_1.collect_entry_fee(self.guest_1, entry_fee)
        self.assertEqual(110.00, self.room_1.till)
        self.assertEqual(10.00, self.guest_1.wallet)

    def test_collect_entry_fee__customer_insufficient_funds(self):
        entry_fee = 10.00
        self.room_1.collect_entry_fee(self.guest_5, entry_fee)
        self.assertEqual(100.00, self.room_1.till)
        self.assertEqual(5.00, self.guest_5.wallet)

    def test_guest_has_sufficient_funds__True(self):
        entry_fee = 10.00
        self.assertEqual(True, self.room_1.check_guest_has_sufficient_funds(self.guest_1, entry_fee))

    def test_guest_has_sufficient_funds__False(self):
        entry_fee = 10.00
        self.assertEqual(False, self.room_1.check_guest_has_sufficient_funds(self.guest_5, entry_fee))

    def test_guest_added_to_guests_owing_fee_list(self):
        entry_fee = 10.00
        self.room_1.collect_entry_fee(self.guest_1, entry_fee)
        self.room_1.collect_entry_fee(self.guest_2, entry_fee)
        self.room_1.collect_entry_fee(self.guest_5, entry_fee)
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_5)
        self.assertEqual(3, len(self.room_1.guest_list))
        self.assertEqual(1, len(self.room_1.guests_owing_fee))

    def test_entry_fee_added_to_guest_tab_if_not_paid_on_entry(self):
        entry_fee = 10.00
        self.room_1.collect_entry_fee(self.guest_1, entry_fee)
        self.room_1.collect_entry_fee(self.guest_2, entry_fee)
        self.room_1.collect_entry_fee(self.guest_5, entry_fee)
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.add_guest_to_room(self.guest_5)
        self.assertEqual(1, len(self.room_1.guests_owing_fee))
        self.assertEqual(10.00, self.guest_5.guest_tab)  
