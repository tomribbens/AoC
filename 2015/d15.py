#!/usr/bin/python3

# 2015 Day 15

import numpy as np

data = np.array([[2,0,-2,0,3], [0,5,-3,0,3],[0,0,5,-1,8],[0,-1,0,5,8]])

score = 0
bscore = 0
for a in range (0,101):
    for b in range(0, 101 - a):
        for c in range(0, 101 - a - b):
            d = 100 - a - b - c

            scores = np.dot(np.array[a, b, c, d], data)
            scores[scores<0] = 0
            score = max(score, scores[0] * scores[1] * scores[2] * scores[3])

            if scores[4] == 500:
                bscore = max(bscore, scores[0] * scores[1] * scores[2] * scores[3])

print(f"Part A: {score}")
print(f"Part B: {bscore}")

