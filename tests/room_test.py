import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Muppet Theatre", 50)

    def test_room_has_name(self):
        self.assertEqual("Muppet Theatre", self.room_1.name)
    
    def test_room_has_max_capacity(self):
        self.assertEqual(50, self.room_1.max_capacity)