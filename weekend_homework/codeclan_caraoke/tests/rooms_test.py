import unittest
from classes.rooms import *
from classes.songs import *
from classes.guests import *

class TestRoom(unittest.TestCase):
    
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
        
    def test_room_has_name(self):
        self.assertEqual("Room1", self.room1.name)

    def test_room_has_playlist(self):
        self.assertNotEqual(0, len(self.room1.playlist))

    def test_room_has_occupants_list(self):
        self.assertEqual(0, len(self.room1.occupants))

    def test_room_has_till(self):
        self.assertEqual(0, self.room1.till)

    def test_room_has_fee(self):
        self.assertEqual(10, self.room1.fee)

    def test__true_can_guest_afford_room_fee(self):
        self.assertEqual(True, self.room1.can_guest_afford_room_fee(self.guest1))

    def test_false_cannot_guest_afford_room_fee(self):
        self.assertEqual(False, self.room1.can_guest_afford_room_fee(self.guest2))

    def test_can_add_money_to_till(self):
        self.assertNotEqual(0, self.room1.add_money_to_till(10))

    def test_check_in_guest_can_afford(self):
        self.room1.check_in_guest(self.guest1)
        self.assertNotEqual(0, len(self.room1.occupants))

    def test_check_out_guest(self):
        self.room1.check_in_guest(self.guest1)
        self.room1.check_out_guest(self.guest1)
        self.assertEqual(0, len(self.room1.occupants))
        
    def test_if_birthday_play_happy_birthday(self):
        self.room1.if_birthday_play_happy_birthday(self.guest1)
        self.assertEqual(7, len(self.room1.playlist))

    def test_if_birthday_play_happy_birthday(self):
        self.room1.if_birthday_play_happy_birthday(self.guest2)
        self.assertEqual(6, len(self.room1.playlist))