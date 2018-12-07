#!/usr/bin/env python3
"""Advent of Code, Day 03"""

import re


REGEX = re.compile("^#(?P<id>\d+) @ (?P<startx>\d+),(?P<starty>\d+): (?P<sizex>\d+)x(?P<sizey>\d+)$")


def part1():
    with open("../data/d03p1.txt", "r") as f:
        data = list(f)

    fabric = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    matches = [REGEX.search(line) for line in data]

    for match in matches:
        startx, starty = int(match.group("startx")), int(match.group("starty"))
        sizex, sizey = int(match.group("sizex")), int(match.group("sizey"))

        for row in range(startx, startx+sizex):
            for col in range(starty, starty+sizey):
                fabric[row][col] += 1

    return sum(sum(1 for item in row if item > 1) for row in fabric)


def part2():
    with open("../data/d03p1.txt", "r") as f:
        data = list(f)

    fabric = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]
    matches = [REGEX.search(line) for line in data]

    for match in matches:
        startx, starty = int(match.group("startx")), int(match.group("starty"))
        sizex, sizey = int(match.group("sizex")), int(match.group("sizey"))

        for row in range(startx, startx + sizex):
            for col in range(starty, starty + sizey):
                fabric[row][col] += 1

    for match in matches:
        startx, starty = int(match.group("startx")), int(match.group("starty"))
        sizex, sizey = int(match.group("sizex")), int(match.group("sizey"))

        overwritten = False

        for row in range(startx, startx + sizex):
            for col in range(starty, starty + sizey):
                if not fabric[row][col] == 1:
                    overwritten = True

        if not overwritten:
            return match.group("id")


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
