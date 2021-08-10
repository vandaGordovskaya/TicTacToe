class Winner:
    __list_of_win_combinations = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7],
                                [2, 5, 8], [3, 4, 5], [6, 7, 8], [2, 4, 6]]

    @property
    def list_of_win_combinations(self):
        return self.__list_of_win_combinations

    def is_winner(self, current_board, player_index):
        is_win = False
        get_current_player_map = [index for index, value in
                                  enumerate(current_board) if value == player_index]
        for list_v in self.list_of_win_combinations:
            count = sum(f in list_v for f in get_current_player_map)
            if count == 3:
                is_win = True
                break
        return is_win
