from classes.guests import *
from classes.songs import *

class Room:
    
    def __init__(self, name, playlist):
        self.name = name
        self.playlist = playlist
        self.fee = 10
        self.till = 0
        self.occupants = []

    def can_guest_afford_room_fee(self, guest):
        if guest.wallet >= self.fee:
            return True
        else:
            return False
        
    def add_money_to_till(self, money):
        self.till += money

    def if_birthday_play_happy_birthday(self, guest):
        if guest.birthday_today == True:
            self.playlist.append("Happy birthday")
    
    def check_in_guest(self, guest):
        if self.can_guest_afford_room_fee(guest) == True and len(self.occupants) <= 5:
            self.occupants.append(guest.name)
            guest.remove_money(self.fee)
            self.add_money_to_till(self.fee)
            self.if_birthday_play_happy_birthday(guest)

    def check_out_guest(self, guest):
        self.occupants.remove(guest.name)
