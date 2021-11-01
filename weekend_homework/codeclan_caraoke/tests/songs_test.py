import unittest
from classes.songs import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Light my fire")
    
    def test_song_has_name(self):
        self.assertEqual("Light my fire", self.song.name)
        