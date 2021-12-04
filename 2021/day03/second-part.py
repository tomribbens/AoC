#!/usr/bin/python3

# Day 3, part 2 of Advent of Code 2021

import sys

input_array = []
with open(str(sys.argv[1])) as f:
    input_array = [line.strip() for line in f]

oxygen = ""
carbondioxide = ""
count = len(input_array)

while count > 1:
    options = [x[len(oxygen)] for x in input_array if x.startswith(oxygen)] 

    if options.count("1") * 2 >= len(options):
        oxygen += "1"
        count = options.count("1")

    else:
        oxygen += "0"
        count = options.count("0")

if len(oxygen) < len(input_array[0]):
    oxygen = [o for o in input_array if o.startswith(oxygen)][0]

count = len(input_array)

while count > 1:
    options = [x[len(carbondioxide)] for x in input_array if x.startswith(carbondioxide)] 

    if options.count("1") * 2 >= len(options):
        carbondioxide += "0"
        count = options.count("0")

    else:
        carbondioxide += "1"
        count = options.count("1")

if len(carbondioxide) < len(input_array[0]):
    carbondioxide = [o for o in input_array if o.startswith(carbondioxide)][0]

print("Result: ", int(oxygen, 2) * int(carbondioxide, 2))    
    



