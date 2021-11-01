import unittest

from classes.guests import Guest
from classes.songs import Song
from classes.rooms import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Paul", 60, "Like a virgin", True)
        self.guest2 = Guest("Iain", 5, "Macarena", False)
        self.guest3 = Guest("Steve", 70, "Under pressure", False)
        self.guest4 = Guest("Debbie", 65, "I will always love you", False)
        self.guest5 = Guest("Carol", 78, "99 red balloons", False)
        self.guest6 = Guest("Anne", 100, "Unbreak my heart", False)
        self.song1 = Song("Sweet Caroline")
        self.song2 = Song("My way")
        self.song3 = Song("Dancing with myself")
        self.song4 = Song("Nutbush City limits")
        self.song5 = Song("Like a virgin")
        self.song6 = Song("Unbreak my heart")
        playlist = [self.song1, self.song2, self.song3, self.song4, self.song5, self.song6]
        self.room1 = Room("Room1", playlist)
        self.room2 = Room("Room2", playlist)
    
    def test_guest_has_name(self):
        self.assertEqual("Paul", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(60, self.guest1.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Like a virgin", self.guest1.favourite_song)

    def test_guest_has_birthday_true(self):
        self.assertEqual(True, self.guest1.birthday_today)

    def test_guest_has_birthday_false(self):
        self.assertEqual(False, self.guest2.birthday_today)

    def test_remove_money(self):
        self.guest1.remove_money(10)
        self.assertEqual(50, self.guest1.wallet)

    def test_omg_my_favourite_song(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual("omg, my favourite song!", self.guest1.omg_my_favourite_song(self.room1.playlist))

