import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("The Muppet Show Theme", "The original show")
        self.song_2 = Song("Mah Na Mah Na", "Film 1")
        self.song_3 = Song("Together Again", "Film 2")
        self.song_4 = Song("Happiness Hotel", "Film 3")
        self.song_5 = Song("It's Not Easy Being Green", "Film 4")
    
    def test_song_has_name(self):
        self.assertEqual("The Muppet Show Theme", self.song_1.name)
    
    def test_song_has_film(self):
        self.assertEqual("The original show", self.song_1.film)
    