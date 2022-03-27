#!/usr/bin/python3

# Day 10

from aocd import get_data

def pascal(line, iterations):
    for _ in range(iterations):
        lastchar = ""
        count = 1
        newline = ""
        for char in line:
            if lastchar == char:
                count += 1
                continue

            newline += str(count if lastchar != "" else "") + lastchar
            lastchar = char
            count = 1

        newline += str(count) + lastchar
        line = newline

    return line


if __name__ == "__main__":
    line = get_data(year=2015, day=10).splitlines()[0]


    print("Part A:", end=" ")
    print(len(pascal(line, 40)))

    
    print("Part B:", end=" ")
    print(len(pascal(line, 50)))

