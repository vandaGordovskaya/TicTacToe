from Game import Game


def main():
    pl1, pl2 = "", ""
    while True:
        my_game = Game(pl1, pl2)
        pl1 = my_game.first_player
        pl2 = my_game.second_player
        my_game.play_game()
        if not my_game.one_more():
            break


if __name__ == '__main__':
    main()
