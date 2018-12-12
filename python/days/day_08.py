#!/usr/bin/env python3
"""Advent of Code, Day 08"""


class Node:
    def __init__(self):
        self.children = []
        self.metadata = []


def _get_data():
    with open("../data/d08p1.txt", "r") as f:
        data = f.read().split()

    return [int(x) for x in data]


def _to_tree(data):
    num_children = data.pop(0)
    num_metadata = data.pop(0)

    children = []
    metadata = []

    for _ in range(num_children):
        children.append(_to_tree(data))

    for _ in range(num_metadata):
        metadata.append(data.pop(0))

    node = Node()
    node.children = children
    node.metadata = metadata
    return node


def part1():
    tree_root = _to_tree(_get_data())

    def add_meta(node):
        return sum(node.metadata) + sum(add_meta(child) for child in node.children)

    return add_meta(tree_root)


def part2():
    tree_root = _to_tree(_get_data())

    def index_val(node):
        if len(node.children) == 0:
            return sum(node.metadata)
        else:
            val = 0
            for idx in node.metadata:
                if idx != 0:
                    try:
                        val += index_val(node.children[idx-1])
                    except IndexError:
                        continue

            return val

    return index_val(tree_root)


if __name__ == "__main__":
    print("part 1:", part1())
    print("part 2:", part2())
