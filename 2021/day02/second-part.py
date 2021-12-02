#!/usr/bin/python3

# Day 2, part 1 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [line.split() for line in input_file]

pos = 0
depth = 0
aim = 0

for i in input_array:
    if i[0] == "forward":
        pos += int(i[1])
        depth += aim * int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    elif i[0] == "up":
        aim -= int(i[1])

print("Result: ", pos*depth)


