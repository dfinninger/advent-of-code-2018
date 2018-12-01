#!/usr/bin/env python3
"""Advent of Code, Day 01"""


def part1():
    with open("data/d01p1.txt", "r") as f:
        data = list(f)

    state = 0
    for item in data:
        if "+" in item:
            item = item.replace("+", "")

        state += int(item)

    return state


def part2():
    with open("data/d01p1.txt", "r") as f:
        data = list(f)

    state = 0
    state_set = {0}

    while True:
        for item in data:
            if "+" in item:
                item = item.replace("+", "")

            state += int(item)
            if state in state_set:
                return state
            state_set.add(state)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
