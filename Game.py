from Board import Board
from Player import Player
from Winner import Winner
from datetime import datetime


class Game:
    first_player = Player("player1", "")
    second_player = Player("player2", "")
    current_player = Player("current", "")
    #play_board
    winner = Winner()
    entered_number: int
    win_score = {first_player: 0, second_player: 0}

    def __init__(self, player1, player2):
        if player1 == "":
            self.initiate_players()
        else:
            self.first_player = player1
            self.second_player = player2
        self.play_board = Board()

    # Define 2 Players
    def initiate_players(self):
        name1 = ""
        index1 = ""
        name2 = ""
        while not name1:
            name1 = input("Player1 name: ")
            if name1:
                self.first_player.set_name(name1)
        while not index1:
            index1 = input("Define your symbol X or O: ")
            if index1 and index1.upper() in "XO":
                self.first_player.set_player_index(index1)
            else:
                index1 = ""
        while not name2:
            name2 = input("Player2 name: ")
            if name2:
                self.second_player.set_name(name2)
        if self.first_player.player_index == "X":
            self.second_player.set_player_index("O")
        else:
            self.second_player.set_player_index("X")

    # Game flow
    def play_game(self):
        self.current_player = self.first_player
        for move in range(1, 10):
            self.player_input(self.current_player.player_index, self.play_board.get_current_board())
            if move > 4 and self.check_win(self.play_board.get_current_board(), self.current_player.player_index):
                break
            elif move == 9:
                self.write_and_show_results(self.current_player.name, True)
            self.switch_player(self.current_player)

    def switch_player(self, current_player):
        if current_player.name == self.first_player.name:
            self.current_player = self.second_player
        else:
            self.current_player = self.first_player

    def player_input(self, player_index, board):

        def check_input_number_and_position():
            while True:
                number = int(input(f'{self.current_player.get_name()} enter your number: '))
                is_free = self.play_board.is_free(number, board)
                if number in range(1, 10) and is_free:
                    self.play_board.current_board = self.play_board.update_board(number, player_index, board)
                    break
                elif number not in range(1, 10):
                    print("Try again and enter correct value!")
                    check_input_number_and_position()
                else:
                    print("This position has filled. Try again and chose other.")
                    check_input_number_and_position()

        check_input_number_and_position()

    def check_win(self, play_board, player_index):
        is_winner = self.winner.is_winner(play_board, player_index)
        is_first_player = (self.first_player.player_index == player_index)
        if is_winner and is_first_player:
            print(self.write_and_show_results(self.first_player.name, draw=False))
            return True
        elif is_winner and is_first_player:
            print(self.write_and_show_results(self.first_player.name, draw=False))
            return True
        else:
            return False

    @staticmethod
    def write_and_show_results(player_name, draw):
        format_date = '%d.%m.%Y %H:%M'
        results_file = open("results.txt", "a")
        if draw:
            results_file.write(f'{datetime.now().strftime(format_date)} - ...Drawn Game... \n')
            results_file.close()
        else:
            results_file.write(f'{datetime.now().strftime(format_date)} - Win {player_name} \n')
            results_file.close()
        results_file = open("results.txt", "r")
        print(results_file.read())
        results_file.close()

    @staticmethod
    def one_more():
        while True:
            answer = input("One more game? Y/N:")
            if answer in "Yy":
                return True
            elif answer in "Nn":
                return False
            else:
                print("Please enter correct letter!")
