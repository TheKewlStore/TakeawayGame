import sys

from takeaway_game.application import TakeawayGame


def main():
    game = TakeawayGame()
    game.run()


if __name__ == '__main__':
    main()
    sys.exit(0)
