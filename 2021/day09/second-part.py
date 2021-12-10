#!/usr/bin/python3

# Day 9, part 1 of Advent of Code 2021

import sys
from collections import defaultdict

def BasinSize(cave, x, y):
    basin = 0
    if cave[x][y] != 0:
        return 0
    else:
        basin += 1
        cave[x][y] = 1

        if x > 0:
            basin += BasinSize(cave, x - 1, y)
        if x + 1 < cave["xsize"]:
            basin += BasinSize(cave, x + 1, y)
        if y > 0:
            basin += BasinSize(cave, x, y - 1)
        if y + 1 < cave["ysize"]:
            basin += BasinSize(cave, x, y + 1)

        return basin


with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]

cave = defaultdict(lambda: defaultdict(int))
total = 0
for i in range(len(input_array)):
    for j in range(len(input_array[i])):
        if input_array[i][j] == "9":
            cave[i][j] = 9

cave["xsize"] = len(input_array)
cave["ysize"] = len(input_array[0])

basinSizes = []
for x in range(cave["xsize"]):
    for y in range(cave["ysize"]):
        size = BasinSize(cave, x, y)
        if size > 0:
            basinSizes.append(size)

print(basinSizes)
basins = 1
biggest = max(basinSizes)
basinSizes.remove(biggest)
basins *= biggest

biggest = max(basinSizes)
basinSizes.remove(biggest)
basins *= biggest

biggest = max(basinSizes)
basinSizes.remove(biggest)
basins *= biggest
print(basins)
        


