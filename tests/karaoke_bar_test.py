import unittest
from classes.karaoke_bar import Karaoke_Bar

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        self.mykaraoke = Karaoke_Bar("CodeClan Caraoke")

    def test_karaoke_bar_has_name(self):
        self.assertEqual("CodeClan Caraoke", self.mykaraoke.name)