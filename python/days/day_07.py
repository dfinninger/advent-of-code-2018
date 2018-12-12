#!/usr/bin/env python3
"""Advent of Code, Day 07"""

NUM_WORKERS = 5
LENGTH_OFFSET = 60

task_length = {
    "A": 0+LENGTH_OFFSET,
    "B": 1+LENGTH_OFFSET,
    "C": 2+LENGTH_OFFSET,
    "D": 3+LENGTH_OFFSET,
    "E": 4+LENGTH_OFFSET,
    "F": 5+LENGTH_OFFSET,
    "G": 6+LENGTH_OFFSET,
    "H": 7+LENGTH_OFFSET,
    "I": 8+LENGTH_OFFSET,
    "J": 9+LENGTH_OFFSET,
    "K": 10+LENGTH_OFFSET,
    "L": 11+LENGTH_OFFSET,
    "M": 12+LENGTH_OFFSET,
    "N": 13+LENGTH_OFFSET,
    "O": 14+LENGTH_OFFSET,
    "P": 15+LENGTH_OFFSET,
    "Q": 16+LENGTH_OFFSET,
    "R": 17+LENGTH_OFFSET,
    "S": 18+LENGTH_OFFSET,
    "T": 19+LENGTH_OFFSET,
    "U": 20+LENGTH_OFFSET,
    "V": 21+LENGTH_OFFSET,
    "W": 22+LENGTH_OFFSET,
    "X": 23+LENGTH_OFFSET,
    "Y": 24+LENGTH_OFFSET,
    "Z": 25+LENGTH_OFFSET
}


class Step:
    def __init__(self, name, constraints=[]):
        self.name = name
        self.constraints = set(constraints)
        self.done = False

    def add_constraint(self, constraint):
        self.constraints.add(constraint)

    def __repr__(self):
        return "Step({}, constraints={{{}}})".format(self.name, ', '.join(self.constraints))


class Worker:
    def __init__(self):
        self.time_in_task = 0
        self.task = None

    def add_time_for_task(self, num):
        self.time_in_task += num

    def work(self):
        if self.time_in_task == 0:
            t = self.task
            self.task = None
            return t
        else:
            self.time_in_task -= 1

    def current_task_name(self):
        if self.task:
            return self.task.name
        else:
            return "-"

    def is_free(self):
        return self.time_in_task == 0

    def __repr__(self):
        return "Worker(time={})".format(self.time_in_task)


def _get_execution_steps():
    with open("../data/d07p1.txt", "r") as f:
        data = list(f)

    deps = [(x[1], x[7]) for x in [y.split() for y in data]]

    uniqs = set()
    for d in deps:
        uniqs.add(d[0])
        uniqs.add(d[1])

    steps = dict()
    for u in uniqs:
        steps[u] = Step(u)

    for dep in deps:
        steps[dep[1]].add_constraint(dep[0])

    return list(steps.values())


def part1():
    execution_order = []
    steps = _get_execution_steps()
    while True:
        candidates = sorted([l for l in steps if len(l.constraints) == 0], key=lambda l: l.name)
        if len(candidates) == 0:
            break

        chosen = candidates[0]
        execution_order.append(chosen.name)

        steps.remove(chosen)

        for l in steps:
            try:
                l.constraints.remove(chosen.name)
            except KeyError:
                pass

    return ''.join(execution_order)


def part2():
    steps = _get_execution_steps()
    workers = [Worker() for _ in range(NUM_WORKERS)]
    iterations = 0

    while True:
        free_workers = [w for w in workers if w.is_free()]
        completed_tasks = [w.work() for w in workers]
        for task in completed_tasks:
            if task is None:
                continue

            for l in steps:
                try:
                    l.constraints.remove(task.name)
                except KeyError:
                    pass

        candidates = sorted([l for l in steps if len(l.constraints) == 0], key=lambda l: l.name)
        if len(steps) == 0 and len(free_workers) == NUM_WORKERS:
            break

        iterations += 1

        for task, worker in zip(candidates, free_workers):
            worker.add_time_for_task(task_length[task.name])
            worker.task = task
            steps.remove(task)

        print(' '.join([w.current_task_name() for w in workers]))
        print(steps)

    return iterations


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
