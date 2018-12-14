#!/usr/bin/env python3
"""Advent of Code, Day 10"""


class Point:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move(self, n=1):
        self.position = (
            self.position[0] + self.velocity[0]*n,
            self.position[1] + self.velocity[1]*n,
        )

    def __repr__(self):
        return "Point({}, {})".format(self.position, self.velocity)


def _get_points():
    with open("../data/d10p1.txt", "r") as f:
        data = list(f)

    points = []
    for line in data:
        pos = int(line[10:16]), int(line[18:24])
        vel = int(line[36:38]), int(line[40:42])
        points.append(Point(pos, vel))

    return points


def _board_size(points):
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for p in points:
        x, y = p.position

        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x

        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    return abs(max_x) + abs(max_y) + abs(min_x) + abs(min_y)


def _move_and_check(points, seconds=0):
    for p in points:
        p.move(seconds)

    while True:
        max_x, min_x = max([p.position[0] for p in points]), min([p.position[0] for p in points])
        max_y, min_y = max([p.position[1] for p in points]), min([p.position[1] for p in points])
        board = [[" " for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]
        for p in points:
            board[p.position[1]-min_y][p.position[0]-min_x] = "#"

        this_size = _board_size(points)
        for p in points:
            p.move()

        if this_size < _board_size(points):
            return board, seconds
        seconds += 1


def part1():
    points = _get_points()
    board, _ = _move_and_check(points, 10360)  # magic number I found by "hand"

    return "\n"+"\n".join(["".join(line) for line in board])


def part2():
    points = _get_points()
    _, seconds = _move_and_check(points, 10360)  # magic number I found by "hand"

    return seconds


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
