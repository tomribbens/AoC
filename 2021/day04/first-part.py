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
        
for i in range(len(drawnNrs)):
    newBoards = [[[None if nr in drawnNrs[0:i] else nr for nr in line]for line in board] for board in boards]

    for board in newBoards:
        transposedBoard = np.array(board).T.tolist()
        for line in board + transposedBoard:
            if all(nr is None for nr in line):
                winningsum = sum([sum(filter(None, winningline)) for winningline in board])
                print(winningsum * drawnNrs[i-1])
                break
        else: continue
        break
    else: continue
    break

