"""The class emulates the logic of TicTacToe game.

    During the initialization of the class, defines players, set start board,
    the board is drawn and the winner is identified as None (unknown).

    Attributes:
        current_player(Player): identifies the temporary variable of
        the Player who does move.
        entered_number(int): the temporary variable for player input.
        first_player(Player): the Player object defines the player who does
        first move.
        second_player(Player): the Player object defines the player who
        does the next move after the first_player.
        current_board(list): the list of values in the cells of the board,
        has default values during initialization.
        winner(str): the temporary variable to store the name of the
        winning player.

    Args:
        player1(Player): the Player object of the first player.
        player2(Player): the Player object of the second player.

"""
from player import Player


class Game:
    current_player = Player(None, None)
    entered_number: int

    def __init__(self, player1, player2):
        self.first_player = player1
        self.second_player = player2
        self.current_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.draw_board()
        self.winner = None

    def play_game(self):
        """Emulate the process of game.

        Identifies the current_player as a first_player at the start of
        the game and set the maximum amount of moves during the game.
        Within the move, takes input from the current player and based on
        the number of done moves(at least 5 for winners) initiates checking
        of game winner or drawn game(when moves is 9 and all cells are
        occupied.
        If the checking is not success, switches players to continue.

        """
        self.current_player = self.first_player
        for move in range(1, 10):
            self.player_input()
            if move > 4 and \
                    self.current_player.is_winner(self.current_board,
                                                  self.current_player.player_index):
                self.winner = self.current_player.get_name()
                break
            elif move == 9:
                self.winner = "...Drawn Game..."
                break
            self.current_player = self.second_player \
                if self.current_player.name == self.first_player.name \
                else self.first_player

    def player_input(self):
        """Get number from the player.

        Asks input from the player and validates if the specified cell number has
        already occupied and the cell number is in acceptable range (from 1 to 9).
        Otherwise send appropriate message:
            if the number out of the range:"Try again and enter correct value!"
            if the cell is occupied: "This position has occupied. Try again and chose other."

        If success, the current_board is updated with the current_player mark in the
        specified by player cell.

        """
        while True:
            number = int(input(f'{self.current_player.get_name()} enter your number: '))
            is_free = False if (str(self.current_board[number - 1])) in "XO" else True
            if number in range(1, 10) and is_free:
                self.current_board[number - 1] = self.current_player.player_index
                self.draw_board()
                break
            elif number not in range(1, 10):
                print("Try again and enter correct value!")
                self.player_input()
            else:
                print("This position has occupied. Try again and chose other.")
                self.player_input()

    def draw_board(self):
        """Drawing current_board.

        """
        index_iterator = 0
        print("_____________")
        for i in range(int(len(self.current_board) / 3)):
            msg = f'| {self.current_board[index_iterator]} | {self.current_board[index_iterator + 1]} |' \
                  f' {self.current_board[index_iterator + 2]} |\n-------------'
            print(msg)
            index_iterator = index_iterator + 3

    @staticmethod
    def one_more():
        """Asks to play one more game.

        The function asks to play one more game and validates input.

        Returns:
            bool: True for success, False otherwise.

        """
        while True:
            answer = input("One more game? Y/N:")
            if answer in "Yy":
                return True
            elif answer in "Nn":
                return False
            else:
                print("Please enter correct letter!")
