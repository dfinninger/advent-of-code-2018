#!/usr/bin/env python3
"""Advent of Code, Day {{day}}"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def _reduce(data):
    while True:
        last_len = len(data)
        for c in ALPHABET:
            data = data.replace(c+c.upper(), "").replace(c.upper()+c, "")

        if last_len == len(data):
            break

    return data


def part1():
    with open("../data/d05p1.txt", "r") as f:
        data = f.read()

    return len(_reduce(data))


def part2():
    with open("../data/d05p1.txt", "r") as f:
        data = f.read()

    results = dict()
    for c in ALPHABET:
        tmp_data = data.replace(c, "").replace(c.upper(), "")
        results[c] = len(_reduce(tmp_data))

    return results[min(results, key=results.get)]


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())

# 10680 low
# 14934 wrong
# 20680 high
