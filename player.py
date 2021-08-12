"""The Player class defines the player in the Game
    Attributes:
        __LIST_OF_WIN_COMBINATIONS(list(lists)): the list of possible
        win combinations lists

    Args:
        name(str) : the player name
        player_index(str): the player mark
"""


class Player:
    __LIST_OF_WIN_COMBINATIONS = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7],
                                [2, 5, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6]]

    def __init__(self, name, player_index):
        self.name = name
        self.player_index = player_index

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def is_winner(self, player_board, player_index):
        """The function defines whether the Player is won or not.

        Args:
            player_board(list): The list of cells values of the board
            player_index(str): The mark of the Player

        Returns:
             is_win(bool): True if success, False otherwise.

        """
        is_win = False
        get_current_player_map = [index for index, value in
                                  enumerate(player_board)
                                  if value == player_index]
        for list_v in self.__LIST_OF_WIN_COMBINATIONS:
            count = sum(f in list_v for f in get_current_player_map)
            if count == 3:
                is_win = True
                break
        return is_win
