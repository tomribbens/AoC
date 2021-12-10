#!/usr/bin/python3

# Day 10, part 1 of Advent of Code 2021

import sys
from collections import deque

points = 0

with open(str(sys.argv[1])) as input_file:
    for line in input_file:
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
                if char == ")":
                    points += 3
                elif char == "]":
                    points += 57
                elif char == "}":
                    points += 1197
                elif char == ">":
                    points += 25137

                break
            else:
                stack.popleft()
print(points)

