#!/usr/bin/python3

# Day 9, part 1 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]

total = 0
for i in range(len(input_array)):
    for j in range(len(input_array[i])):
        if i > 0:
            if not int(input_array[i][j]) < int(input_array[i-1][j]):
                continue
        if i + 1 < len(input_array):
            if not int(input_array[i][j]) < int(input_array[i+1][j]):
                continue
        if j > 0:
            if not int(input_array[i][j]) < int(input_array[i][j-1]):
                continue
        if j + 1 < len(input_array[i]):
            if not int(input_array[i][j]) < int(input_array[i][j+1]):
                continue

        total += int(input_array[i][j]) + 1

print(total)
        


