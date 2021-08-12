from game import Game
from player import Player
from datetime import datetime


def main():
    counter = 0
    sets = {}

    def initiate_players():
        name_pl1 = index_pl1 = name_pl2 = None
        while not name_pl1:
            name1 = input("Player1 name: ")
            if name1:
                name_pl1 = name1
        while not index_pl1:
            index1 = input("Define your symbol X or O: ")
            index_pl1 = index1.upper() if index1 and index1.upper() in "XO" else None
        while not name_pl2:
            name2 = input("Player2 name: ")
            if name2:
                name_pl2 = name2
        pl_1 = Player(name_pl1, index_pl1)
        index_pl2 = "X" if index_pl1 == "O" else "O"
        pl_2 = Player(name_pl2, index_pl2)
        return pl_1, pl_2

    def write_and_show_results(winner):
        format_date = '%d.%m.%Y %H:%M'
        if any(sets) < 1:
            results_file1 = open("results.txt", "a")
            results_file1.write(f'{datetime.now().strftime(format_date)} - Win {winner} \n')
        else:
            results_file1 = open("results.txt", "w")
            for k, v in sets.items():
                results_file1.write(f'Set #{k} : win - {v}\n')
        results_file1.close()
        results_file2 = open("results.txt")
        print(results_file2.read())
        results_file2.close()

    pl1, pl2 = initiate_players()

    while True:
        counter += 1
        my_game = Game(pl1, pl2)
        my_game.play_game()
        sets[counter] = my_game.winner
        write_and_show_results(my_game.winner)
        if not my_game.one_more():
            # clear log files
            results_file = open("results.txt", "w")
            results_file.write("")
            results_file.close()
            break


if __name__ == '__main__':
    main()
