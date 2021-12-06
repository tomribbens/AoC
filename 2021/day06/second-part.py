#!/usr/bin/python3

# Day 6, part 1 of Advent of Code 2021

import sys
from collections import defaultdict

with open(str(sys.argv[1])) as input_file:
    input_array = list(map(int, input_file.readline().strip().split(","))) 

fish = defaultdict(int)
for i in input_array:
    fish[i] += 1

for day in range(int(sys.argv[2])):
    newFish = defaultdict(int)
    for generation in fish.items():
        if generation[0] == 0:
            newFish[8] += generation[1]
            newFish[6] += generation[1]
        else:
            newFish[generation[0] - 1] += generation[1]

    fish = newFish


print(sum(fish.values()))
