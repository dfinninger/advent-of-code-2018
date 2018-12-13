#!/usr/bin/env python3
"""Advent of Code, Day 09"""

from collections import defaultdict, deque


def _get_constraints():
    with open("../data/d09p1.txt", "r") as f:
        data = f.read().split()

    return int(data[0]), int(data[6])


# had to look up the solution: https://www.reddit.com/r/adventofcode/comments/a4i97s/2018_day_9_solutions/ebepyc7
# turns out I had an off-by-one error
def _play(num_players, last_marble):
    game_board = deque([0])
    players = defaultdict(int)

    for marble_value in range(1, last_marble+1):
        if marble_value % 23 == 0:
            game_board.rotate(7)
            players[marble_value % num_players] += marble_value + game_board.pop()
            game_board.rotate(-1)
        else:
            game_board.rotate(-1)
            game_board.append(marble_value)

    return max(players.values())


def part1():
    return _play(*_get_constraints())


def part2():
    num_players, last_marble = _get_constraints()
    return _play(num_players, last_marble*100)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())

# 290904 low
