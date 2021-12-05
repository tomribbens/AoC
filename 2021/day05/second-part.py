#!/usr/bin/python3

# Day 5, part 2 of Advent of Code 2021

import sys

def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v

def AddToPosition(vents, x, y):
    if not x in vents:
        vents[x] = {}

    if not y in vents[x]:
        vents[x][y] = 0

    vents[x][y] += 1

    return

with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]


vents = {}

toDraw = [[[int(x) for x in coords.split(",")] for coords in line.split(" -> ")] for line in input_array]

for line in toDraw:
    if line[0][0] == line[1][0]:
        for i in range(min(line[0][1],line[1][1]),max(line[0][1],line[1][1])+1):
            AddToPosition(vents, line[0][0], i)

    elif line[0][1] == line[1][1]:
        for i in range(min(line[0][0],line[1][0]),max(line[0][0],line[1][0])+1):
            AddToPosition(vents, i, line[0][1])

    else:
        if line[0][0] < line[1][0]:
            if line[0][1] < line[1][1]:
                for i in range(line[1][0] - line[0][0] + 1):
                    AddToPosition(vents, line[0][0] + i, line[0][1] + i)
            else:
                for i in range(line[1][0] - line[0][0] + 1):
                    AddToPosition(vents, line[0][0] + i, line[0][1] - i)

        else:
            if line[0][1] < line[1][1]:
                for i in range(line[1][1] - line[0][1] + 1):
                    AddToPosition(vents, line[0][0] - i, line[0][1] + i)
            else:
                for i in range(line[0][0] - line[1][0] + 1):
                    AddToPosition(vents, line[0][0] - i, line[0][1] - i)
                    




count = sum(i > 1 for i in list(NestedDictValues(vents)))
print(count)
    

        

