#!/usr/bin/python3

# Day 8, part 1 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [[digit.strip().split(' ') for digit in line.strip().split('|')] for line in input_file] 

count = 0
for i in input_array:
    for j in i[1]:
        if len(j) == 2 or len(j) == 4 or len(j) == 3 or len(j) == 7:
            count += 1



print(count)

