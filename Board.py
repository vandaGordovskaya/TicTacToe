class Board:
    default_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_board = default_board

    def __init__(self):
        self.draw_board(self.default_board)

    def get_current_board(self):
        return self.current_board

    def set_current_board(self, board):
        self.current_board = board

    def get_default_board(self):
        return self.default_board

    @staticmethod
    def draw_board(board):
        index_iterator = 0
        print("_____________")
        for i in range(int(len(board) / 3)):
            msg = f'| {board[index_iterator]} | {board[index_iterator + 1]} |' \
                  f' {board[index_iterator + 2]} |\n-------------'
            print(msg)
            index_iterator = index_iterator + 3

    @staticmethod
    def is_free(position, board):
        if (board[position - 1]) == "X" or (board[position - 1]) == "O":
            return False
        else:
            return True

    def update_board(self, position, player_index, board):
        if self.is_free(position, board):
            self.current_board[position - 1] = player_index
            self.draw_board(self.current_board)
        return self.current_board

    def clear_board(self):
        self.current_board = self.default_board
        self.draw_board(self.get_default_board())
