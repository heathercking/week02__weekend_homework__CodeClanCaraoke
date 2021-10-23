class Guest:

    def __init__(self, name, age, wallet, entry_fee_paid):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.entry_fee_paid = entry_fee_paid

    def pay_entry_fee(self, input_fee):
        self.wallet -= input_fee
    
    def favourite_song_reaction(self):
        return "Yaaaas"


    