#!/usr/bin/python3

# Day 1, part 2 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [int(line) for line in input_file]

count = 0
i = 3  # Starting at the 4th element, comparing it to the first

while i < len(input_array):
    if input_array[i] > input_array[i-3]:
        count += 1

    i += 1
    

print("Result: ", count)
