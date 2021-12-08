#!/usr/bin/python3

# Day 8, part 2 of Advent of Code 2021

import sys

with open(str(sys.argv[1])) as input_file:
    input_array = [[digit.strip().split(' ') for digit in line.strip().split('|')] for line in input_file] 

digits= {}
digits[0] = set("abcefg")
digits[1] = set("cf")
digits[2] = set("acdeg")
digits[3] = set("acdfg")
digits[4] = set("bcdf")
digits[5] = set("abdfg")
digits[6] = set("abdefg")
digits[7] = set("acf")
digits[8] = set("abcdefg")
digits[9] = set("abcdfg")

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

    solution = {}

    solution['a'] = examples[2].symmetric_difference(examples[3])
    solution['d'] = examples[4].intersection(examples[5][0]).intersection(examples[5][1]).intersection(examples[5][2])
    solution['b'] = examples[4].symmetric_difference(examples[2]).symmetric_difference(solution['d'])
    
    for x in examples[6]:
        if not solution['d'].issubset(x):
            continue
        elif examples[2].issubset(x):
            solution['e'] = x.symmetric_difference(examples[7])
        else:
            solution['c'] = x.symmetric_difference(examples[7])

    solution['f'] = solution['c'].symmetric_difference(examples[2])
    solution['g'] = examples[7].symmetric_difference(solution['a']).symmetric_difference(solution['b']).symmetric_difference(solution['c']).symmetric_difference(solution['d']).symmetric_difference(solution['e']).symmetric_difference(solution['f'])


    search = ""
    replace = ""
    for k, s in dict(solution).items():
        replace += k
        search += ''.join(s)

    trTable = str().maketrans(search, replace)


    display = ""
    for j in i[1]:
        toTest = j.translate(trTable)

        for d,segments in digits.items():
            if set(toTest) == segments:
                display += str(d)
                break


    total += int(display)



print(total)
