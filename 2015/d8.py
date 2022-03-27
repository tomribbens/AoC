#!/usr/bin/python3

# Day 5

from aocd import get_data
import re


if __name__ == "__main__":
    lines = get_data(year=2015, day=8).splitlines()

    print("Part A:", end=" ")

    stringcode = 0
    stringmem = 0
    stringexpand = 0

    for line in lines:
        stringcode += len(line)
        stringmem += len(bytes(line[1:-1], "utf-8").decode("unicode_escape"))
        stringexpand += len(line) + line.count('"') + line.count('\\') + 2

    print(stringcode - stringmem)

    
    
    print("Part B:", end=" ")
    print(stringexpand - stringcode)

