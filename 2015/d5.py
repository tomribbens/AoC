#!/usr/bin/python3

# Day 5

from aocd import lines
import re

def niceA(line):
    if any(x in line for x in ["ab", "cd", "pq", "xy"]):
        return False

    if not re.search(r'([a-z])\1', line):
        return False

    if len(re.findall(r'[aoeiu]', line)) < 3:
        return False

    return True


def niceB(line):
    if not re.search(r'([a-z][a-z]).*\1', line):
        return False

    if not re.search(r'([a-z])[a-z]\1', line):
        return False

    return True

if __name__ == "__main__":
    print("Part A:", end=" ")
    print(sum(niceA(line) for line in lines))
    print("Part B:", end=" ")
    print(sum(niceB(line) for line in lines))
