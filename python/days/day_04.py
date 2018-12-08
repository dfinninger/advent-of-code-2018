#!/usr/bin/env python3
"""Advent of Code, Day 04"""

from collections import defaultdict
from datetime import datetime
import re


REGEX = re.compile("^\[(?P<datetime>.*)\] (?P<event>.*)$")


def _gen_guard_schedules():
    with open("../data/d04p1.txt", "r") as f:
        data = list(f)

    matches = [REGEX.search(line) for line in data]

    events = sorted([
        (datetime.strptime(match.group("datetime"), "%Y-%m-%d %H:%M"), match.group("event"))
        for match in matches
    ])

    guard_schedules = defaultdict(lambda: [0 for _ in range(0, 60)])

    active_guard = 0
    sleep_time = 0
    for time, event in events:
        if "Guard" in event:
            active_guard = int(event.split()[1].replace("#", ""))
            continue

        if "falls asleep" in event:
            sleep_time = time.minute
        elif "wakes up" in event:
            for i in range(sleep_time, time.minute):
                guard_schedules[active_guard][i] += 1

    return guard_schedules


def part1():
    guard_schedules = _gen_guard_schedules()

    sleepiest_guard = max(guard_schedules, key=lambda x: sum(guard_schedules[x]))
    sleepiest_minute = guard_schedules[sleepiest_guard].index(max(guard_schedules[sleepiest_guard]))

    return sleepiest_guard * sleepiest_minute


def part2():
    guard_schedules = _gen_guard_schedules()

    consistent_guard = max(guard_schedules, key=lambda x: max(guard_schedules[x]))
    sleepiest_minute = guard_schedules[consistent_guard].index(max(guard_schedules[consistent_guard]))

    return consistent_guard * sleepiest_minute


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
