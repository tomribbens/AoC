#!/usr/bin/python3

# Day 6, part 1 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = list(map(int, input_file.readline().strip().split(","))) 

for day in range(int(sys.argv[2])):
    for toAdd in range(input_array.count(0)):
        input_array.append(9)

    input_array = [x if x > 0 else 7 for x in input_array]
    input_array = [x - 1 for x in input_array]

print(len(input_array))

