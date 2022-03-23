#!/usr/bin/python3

# Day 3, part 2 of Advent of Code 2015

from aocd import get_data
data = get_data(day=3, year=2015)

# Initiate set of visited locations with the starting location
visited = {(0,0)}
santa_current = (0,0)
robo_current = (0,0)

for idx, char in enumerate(data):
    if idx % 2:
        current = santa_current
    else:
        current = robo_current

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

    if idx % 2:
        santa_current = current 
    else:
        robo_current = current

print(len(visited))

