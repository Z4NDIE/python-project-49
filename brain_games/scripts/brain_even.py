#!/usr/bin/env python3

from brain_games.engine import game_start
from brain_games.games import even


def main():
    game_start(even)


if __name__ == '__main__':
    main()
