// Day 01

use std::collections::HashSet;

pub fn part1() {
    let input = include_str!("data/d01p1.txt");
    let x: i32 = input.lines()
        .map(|i: &str| i.parse::<i32>().unwrap())
        .sum();

    println!("part 1: {}", x);
}

pub fn part2() {
    let input = include_str!("data/d01p1.txt");
    let endless = input.lines()
        .map(|i: &str| i.parse::<i32>().unwrap())
        .cycle();

    let mut state = 0;
    let mut states = HashSet::new();
    for item in endless {
        state += item;
        if ! states.insert(state) {
            println!("part 2: {}", state);
            return
        }
    }
}