class Room:
    
    def __init__(self, input_name, input_max_capacity):
        self.name = input_name
        self.max_capacity = input_max_capacity
        self.guest_list = []
        self.free_spaces = 0
        self.song_list = []


    def add_guest_to_room(self, input_guest):
        self.guest_list.append(input_guest)

    def remove_guest_from_room(self, input_guest):
        self.guest_list.remove(input_guest)

        # for person in self.guest_list:
        #     print(person.name)
    
    def add_song_to_room(self, input_song):
        self.song_list.append(input_song)
    
    