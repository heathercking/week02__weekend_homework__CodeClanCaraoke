class Room:
    
    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.guest_list = []
        self.free_spaces = 0
