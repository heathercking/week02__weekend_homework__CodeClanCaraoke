class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def pay_entry_fee(self, input_fee):
        self.wallet -= input_fee
    
    def favourite_song_reaction(self):
        return "Yaaaas"


    