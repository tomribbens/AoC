#!/usr/bin/python3

# Day 8, part 2 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [[digit.strip().split(' ') for digit in line.strip().split('|')] for line in input_file] 

total = 0
for i in input_array:
    examples = {}
    examples[5] = []
    examples[6] = []

    for j in i[0]:
        if len(j) == 2:
            examples[2] = set(j)
        elif len(j) == 3:
            examples[3] = set(j)
        elif len(j) == 4:
            examples[4] = set(j)
        elif len(j) == 5:
            examples[5].append(set(j)) 
        elif len(j) == 6:
            examples[6].append(set(j))
        elif len(j) == 7:
            examples[7] = set(j)

    digits = {}
    # A digit with two segments is a one, three segments is a seven, four segments is a four, and 7 segments is an eight
    digits[1] = examples[2]
    digits[7] = examples[3]
    digits[4] = examples[4]
    digits[8] = examples[7]

    for ex in examples[5]:
        # Of the 5 segment digits, only a three shares two segments with a one
        if len(ex.intersection(digits[1])) == 2:
            digits[3] = ex
        elif len(ex.intersection(digits[4])) == 3:
            digits[5] = ex
        elif len(ex.intersection(digits[4])) == 2:
            digits[2] = ex


    for ex in examples[6]:
        if len(ex.intersection(digits[1])) == 1:
            digits[6] = ex
        elif len(ex.intersection(digits[4])) == 4:
            digits[9] = ex
        elif len(ex.intersection(digits[4])) == 3:
            digits[0] = ex

    output = ""

    for j in i[1]:
        for d,segs in digits.items():
            if set(segs) == set(j):
                output += str(d)
                break

    total += int(output)
    
print(total)
