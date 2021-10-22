import unittest
from classes.karaoke_bar import Karaoke_Bar
from classes.room import Room
from classes.guest import Guest

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.mykaraoke = Karaoke_Bar("CodeClan Caraoke")

        self.room_1 = Room("Muppet Theatre", 5)
        self.room_2 = Room("The Stage", 3)
        self.room_3 = Room("The Attic", 2)

        self.guest_1 = Guest("Kermit the Frog", 32, 20.00)
        self.guest_2 = Guest("Miss Piggy", 29, 10.00)
        self.guest_3 = Guest("Fozzie the Bear", 40, 15.00)
        self.guest_4 = Guest("Beaker", 17, 30.00)
        self.guest_5 = Guest("The Swedish Chef", 35, 5.00)


    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.mykaraoke.name)
    
    # def test_capacity_of_all_rooms(self):
    #     self.room_1.add_guest_to_room
    #     all_rooms = [self.room_1, self.room_2, self.room_3]

        


