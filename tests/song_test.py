import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("The Muppet Show Theme")
        self.song_2 = Song("Mah Na Mah Na")
        self.song_3 = Song("Together Again")
        self.song_4 = Song("Happiness Hotel")
        self.song_5 = Song("It's Not Easy Being Green")
    
    def test_song_has_name(self):
        self.assertEqual("The Muppet Show Theme", self.song_1.name)
    