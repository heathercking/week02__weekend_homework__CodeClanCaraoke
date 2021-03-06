class Bar:
    
    def __init__(self, input_name, till):
        self.name = input_name
        self.till = till
        self.bar_tab = 0
        self.drinks_inventory = []


    def check_guest_is_old_enough_to_drink(self, input_guest):
        return input_guest.age >= 18

    def serve_guest_drink(self, input_pay_by_tab, input_guest, input_drink):
        if self.check_guest_is_old_enough_to_drink(input_guest) == True:
            if self.add_drink_to_tab_check(input_pay_by_tab) == True:
                input_guest.guest_tab += input_drink.price
            else:
                input_guest.buy_drink(input_drink)
                self.till += input_drink.price
        
    def add_drink_to_tab_check(self, user_input):
        if user_input == "yes":
            return True
        else:
            return False

    def add_new_drink_to_stock(self, input_drink):
        self.drinks_inventory.append(input_drink)
    
    def increase_stock_level_of_a_drink(self, input_drink, input_quantity):
        input_drink.stock_level += input_quantity
    
    def get_total_drinks_stock_level(self):
        total_stock = 0
        for drink in self.drinks_inventory:
            total_stock += drink.stock_level
            print(f'{drink.name} = {drink.stock_level}')
        return total_stock
    
    def get_total_value_of_drinks_stock(self):
        total_value = 0
        for drink in self.drinks_inventory:
            total_value += drink.price * drink.stock_level
        return total_value
