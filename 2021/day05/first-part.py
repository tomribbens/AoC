#!/usr/bin/python3

# Day 5, part 1 of Advent of Code 2021

import sys

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]


vents = {}

toDraw = [[[int(x) for x in coords.split(",")] for coords in line.split(" -> ")] for line in input_array]

for line in toDraw:
    if line[0][0] == line[1][0]:
        for i in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
            if not line[0][0] in vents:
                vents[line[0][0]] = {}

            if not i in vents[line[0][0]]:
                vents[line[0][0]][i] = 0

            vents[line[0][0]][i] += 1

    elif line[0][1] == line[1][1]:
        for i in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
            if not i in vents:
                vents[i] = {}

            if not line[0][1] in vents[i]:
                vents[i][line[0][1]] = 0

            vents[i][line[0][1]] += 1


count = sum(i > 1 for i in list(NestedDictValues(vents)))
print(count)
    

        

