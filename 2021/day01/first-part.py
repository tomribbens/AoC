#!/usr/bin/python3

# Day 1, part 1 of Advent of Code 2021

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    input_array = [int(line) for line in input_file]

previous = input_array[0]
count = 0
for i in input_array[1:]:
    if previous < i:
        count += 1

    previous = i 


print("Result: ", count)
