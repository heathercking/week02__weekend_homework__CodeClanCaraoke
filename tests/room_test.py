import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Muppet Theatre", 50)

        self.guest_1 = Guest("Kermit the Frog", 32)
        self.guest_2 = Guest("Miss Piggy", 29)
        self.guest_3 = Guest("Fozzie the Bear", 40)
        self.guest_4 = Guest("Beaker", 17)
        self.guest_5 = Guest("The Swedish Chef", 35)

        self.song_1 = Song("The Muppet Show Theme")
        self.song_2 = Song("Mah Na Mah Na")
        self.song_3 = Song("Together Again")
        self.song_4 = Song("Happiness Hotel")
        self.song_5 = Song("It's Not Easy Being Green")


    def test_room_has_name(self):
        self.assertEqual("Muppet Theatre", self.room_1.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(50, self.room_1.max_capacity)
    
    def test_add_guest_to_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))
    
    def test_remove_guest_from_room(self):
        self.room_1.add_guest_to_room(self.guest_1)
        self.room_1.add_guest_to_room(self.guest_2)
        self.room_1.remove_guest_from_room(self.guest_1)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_add_song_to_room(self):
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(1, len(self.room_1.song_list))