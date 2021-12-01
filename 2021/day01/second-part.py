#!/usr/bin/python

# Day 1, part 2 of Advent of Code 2021

import sys

input_array = []
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        input_array.append(int(line))

count = 0
i = 3

while i < len(input_array):
    if input_array[i] + input_array[i-1] + input_array[i-2] > input_array[i-1] + input_array[i-2] + input_array[i-3]:
        count += 1

    i += 1
    

print("Result: ", count)
