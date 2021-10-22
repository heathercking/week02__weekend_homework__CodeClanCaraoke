class Guest:

    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet

    def pay_entry_fee(self, input_fee):
        # if self.check_sufficient_funds:
        if self.wallet >= input_fee:
            self.wallet -= input_fee
        else:
            print("Goodbye!")
    
    def check_sufficient_funds(self, input_fee):
        if self.wallet >= input_fee:
            return True
        else:
            return False