#!/usr/bin/python3

# Day 3, part 1 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [[char for char in line.strip()] for line in input_file]


counts = [0] * len(input_array[0])
for i in input_array:
    for idx, digit in enumerate(i):
        if digit == '1':
            counts[idx] += 1

gamma = 0
pos = 1

for count in reversed(counts):
    if count * 2 > len(input_array):
        gamma += pos

    pos *= 2



print("Result: ", gamma * ((2**len(input_array[0]) - 1) ^ gamma))
