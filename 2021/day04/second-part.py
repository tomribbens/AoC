#!/usr/bin/python3

# Day 4, part 1 of Advent of Code 2021

import sys
import numpy as np

boards = []
idx = 0
drawnNrs = []
with open(str(sys.argv[1])) as input_file:
    drawnNrs = list(map(int, input_file.readline().split(',')))
    input_file.readline()  # get past the blank line following the drawn numbers

    for line in input_file:
        if line.strip() == "":
            idx += 1
        else:
            if not len(boards) > idx:
                boards.append([])

            boards[idx].append(list(map(int, line.split())))
        
for i in drawnNrs:
    boards = [[[None if nr == i else nr for nr in line]for line in board] for board in boards]

    for board in list(boards):
        transposedBoard = np.array(board).T.tolist()
        for line in board + transposedBoard:
            if all(nr is None for nr in line):
                if len(boards) == 1:
                    winningsum = sum([sum(filter(None, winningline)) for winningline in boards[0]])
                    print("Result: ", winningsum * i)
                    break
                elif board in boards:
                    boards.remove(board)
        else: continue
        break
    else: continue
    break
