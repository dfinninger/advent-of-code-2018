#!/usr/bin/env python3
"""Advent of Code, Day 01"""

from itertools import cycle


def part1():
    with open("../data/d01p1.txt", "r") as f:
        data = list(f)

    return sum([int(x) for x in data])


def part2():
    with open("../data/d01p1.txt", "r") as f:
        data = list(f)

    state = 0
    state_set = {0}

    for item in cycle(data):
        state += int(item)
        if state in state_set:
            return state
        state_set.add(state)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
