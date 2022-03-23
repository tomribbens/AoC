#!/usr/bin/python3

# Day 3, part 1 of Advent of Code 2015

from aocd import get_data
data = get_data(day=3, year=2015)

# Initiate set of visited locations with the starting location
visited = {(0,0)}
current = (0,0)

for char in data:
    if char == ">":
        current = ( current[0] + 1, current[1])
    elif char == "<":
        current = ( current[0] - 1, current[1])
    elif char == "v":
        current = ( current[0], current[1] - 1)
    elif char == "^":
        current = ( current[0], current[1] + 1)
    else:
        print("Unknown Character: " + char)

    visited.add(current)

print(len(visited))

