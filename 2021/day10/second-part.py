#!/usr/bin/python3

# Day 10, part 1 of Advent of Code 2021

import sys
import math
from collections import deque

scores = []

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        badline = False
        stack = deque()
        for char in line.strip():
            if char == "(":
                stack.appendleft(")")
            elif char == "[":
                stack.appendleft("]")
            elif char == "{":
                stack.appendleft("}")
            elif char == "<":
                stack.appendleft(">")
            elif char != stack[0]:
                badline = True
                break
            else:
                stack.popleft()

        if badline == True:
            continue

        linescore = 0
        while stack:
            char = stack.popleft()
            linescore *= 5
            if char == ")":
                linescore += 1
            elif char == "]":
                linescore += 2
            elif char == "}":
                linescore += 3
            elif char == ">":
                linescore += 4

        scores.append(linescore)

print(scores)
scores.sort()
print(scores)
middle = math.ceil(len(scores) / 2) - 1
print(middle)
print(scores[middle])
