class Room:
    
    def __init__(self, input_name, input_max_capacity):
        self.name = input_name
        self.max_capacity = input_max_capacity
        self.guest_list = []
        self.free_spaces = self.max_capacity - len(self.guest_list)
        self.song_list = []


    def add_guest_to_room(self, input_guest):
        if self.free_spaces > 0:
            self.guest_list.append(input_guest)
            self.free_spaces -= 1
        else:
            print("Sorry, not enough space.")   

    # def add_guest_to_room(self, input_guests):
    #     if self.free_spaces > 0:
    #         for guest in input_guests:
    #             self.guest_list.append(guest)
    #             self.free_spaces -= 1
    #     else:
    #         print("Sorry, not enough space.")   

    def remove_guest_from_room(self, input_guest):
        self.guest_list.remove(input_guest)
        self.free_spaces += 1
    
    def add_song_to_room(self, input_song):
        self.song_list.append(input_song)
    
    def remove_song_from_room(self, input_song):
        self.song_list.remove(input_song)
    
    def check_room_has_capactiy(self, input_number_of_guests):
        if input_number_of_guests <= self.free_spaces:
            return True
        else:
            return False

    def view_room_song_list(self):
        for song in self.song_list:
            print(song.name)

    def favourite_song_check(self, input_song):
        for song in self.song_list:
            if input_song == song:
                return "Yaaaas"
            # if input_song != song:
            #     return "No"

    
        
    
