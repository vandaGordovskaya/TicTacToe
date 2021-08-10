class Player:
    name: str
    player_index: str

    def __init__(self, name, player_index):
        self.name = name
        self.player_index = player_index

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def set_player_index(self, player_index):
        if player_index == "X":
            self.player_index = "X"
        else:
            self.player_index = "O"


