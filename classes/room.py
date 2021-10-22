class Room:
    
    def __init__(self, input_name, input_max_capacity):
        self.name = input_name
        self.max_capacity = input_max_capacity
        self.guest_list = []
        self.free_spaces = self.max_capacity - len(self.guest_list)
        self.waiting_list = []
        self.song_list = []


    def add_guest_to_room(self, input_guest):
        self.guest_list.append(input_guest)
        self.free_spaces -= 1

    def remove_guest_from_room(self, input_guest):
        self.guest_list.remove(input_guest)
        self.free_spaces += 1
    
    def add_song_to_room(self, input_song):
        self.song_list.append(input_song)
    
    def remove_song_from_room(self, input_song):
        self.song_list.remove(input_song)
    
    def check_room_has_capactiy(self, input_number_of_guests):
        self.free_spaces = self.max_capacity - len(self.guest_list)
        if input_number_of_guests <= self.free_spaces:
            return True
        else:
            print("Sorry, not enough space. Would you like to try another room?")
            return False


