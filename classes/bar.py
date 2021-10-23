class Bar:
    
    def __init__(self, input_name, till):
        self.name = input_name
        self.till = till
        self.bar_tab = 0
        self.drinks_inventory = []


    def check_guest_is_old_enough_to_drink(self, input_guest):
        return input_guest.age >= 18

    def serve_guest_drink(self, input_guest, input_drink):
        if self.check_guest_is_old_enough_to_drink(input_guest) == True:
            if self.add_drink_to_tab_check() == True:
                input_guest.guest_tab += input_drink.price
            else:
                input_guest.buy_drink(input_drink)
                self.till += input_drink.price
        
    def add_drink_to_tab_check(self):
        pay_by_tab = input("Would you like to add this to your tab? ")
        if pay_by_tab == "yes":
            return True
        else:
            return False

    def add_new_drink_to_stock(self, input_drink):
        self.drinks_inventory.append(input_drink)