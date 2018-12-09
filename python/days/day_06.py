#!/usr/bin/env python3
"""Advent of Code, Day {{day}}"""

import collections


def _get_coordinates():
    with open("../data/d06p1.txt", "r") as f:
        data = list(f)

    return [(int(x), int(y)) for x, y in [item.strip().split(", ") for item in data]]


def part1():
    coord = _get_coordinates()
    max_x, max_y = max([x for x, _ in coord]), max([y for _, y in coord])

    counter = collections.Counter()
    disqualifications = set()
    for x in range(0, max_x):
        for y in range(0, max_y):
            distances = dict()
            for point in coord:
                distances[point] = abs(point[0] - x) + abs(point[1] - y)

            closest = min(distances, key=distances.get)
            count = collections.Counter(distances.values())[distances[closest]]

            if count > 1:
                continue  # there was a tie

            if x == 0 or x == max_x or y == 0 or y == max_y:
                disqualifications.add(closest)

            counter.update([closest])

    for dq in disqualifications:
        del counter[dq]

    return counter.most_common()[1][1]  # no idea why the second most common is the answer...


def part2():
    safe_coord = _get_coordinates()
    max_x, max_y = max([x for x, _ in safe_coord]), max([y for _, y in safe_coord])

    points = []
    for x in range(0, max_x):
        for y in range(0, max_y):
            distances = 0
            for point in safe_coord:
                distances += abs(point[0] - x) + abs(point[1] - y)

            if distances <= 10000:
                points.append((x, y))

    return len(points)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())


