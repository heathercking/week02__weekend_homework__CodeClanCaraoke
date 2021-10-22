import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Muppet Theatre", 50)
        