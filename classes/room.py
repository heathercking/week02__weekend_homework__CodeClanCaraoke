class Room:
    
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guest_list = []
        self.free_spaces = 0


    def add_guest_to_room(self, guest):
        self.guest_list.append(guest)
    
    def remove_guest_from_room(self, guest):
        self.guest_list.remove(guest)