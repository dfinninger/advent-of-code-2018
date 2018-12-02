#!/usr/bin/env python3
"""Advent of Code, Day 02"""

from collections import Counter


def part1():
    with open("../data/d02p1.txt", "r") as f:
        data = list(f)

    counters = [Counter(item) for item in data]

    twos = [any([item == 2 for _, item in c.items()]) for c in counters]
    threes = [any([item == 3 for _, item in c.items()]) for c in counters]

    return sum(twos) * sum(threes)


def part2():
    with open("../data/d02p1.txt", "r") as f:
        data = list(f)

    for index, outer in enumerate(data):
        for inner in data[index+1:]:
            if sum([o == i for o, i in zip(outer, inner)]) == (len(outer) - 1):
                return "".join([o for o, i in zip(outer, inner) if o == i])


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
