class Guest:
    
    def __init__(self, name, wallet, favourite_song, birthday_today):
        self.name = name
        self.wallet = wallet
        self.birthday_today = birthday_today
        self.favourite_song = favourite_song
        
    def remove_money(self, money):
        self.wallet -= money

    def omg_my_favourite_song(self, playlist):
        for song in playlist:
            if self.favourite_song == song.name:
                return "omg, my favourite song!"