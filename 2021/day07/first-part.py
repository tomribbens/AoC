#!/usr/bin/python3

# Day 7, part 1 of Advent of Code 2021

import sys
import statistics

with open(str(sys.argv[1])) as input_file:
    input_array = list(map(int, input_file.readline().strip().split(","))) 

fuel = 0
horizontal = statistics.median(input_array)

for i in input_array:
    fuel += abs(i - horizontal)

print(fuel)

