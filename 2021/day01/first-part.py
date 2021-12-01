#!/usr/bin/python

# Day 1, part 1 of Advent of Code 2021

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(int(line))

previous = -1
count = 0
for i in input_array:
    if previous < i and previous != -1:
        count += 1

    previous = i 


print("Result: ", count)
