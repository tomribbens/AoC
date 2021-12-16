#!/usr/bin/python3

# Day 16, part 1 of Advent of Code 2021

import sys
import binascii
from math import prod

input_array = []
with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]


for line in input_array:
    binstring = ''.join([format(int(x, 16), '04b') for x in line])


    # Stack contains lists of [ length type, remaining length, operator type, values[] ]
    stack = [["s", 0, "s", []]]
    binpos = 0
    totalversion = 0
    while stack:
        version = int(binstring[binpos:binpos+3], 2)
        binpos += 3
        typeid = int(binstring[binpos:binpos+3], 2)
        binpos += 3
        totalbits = 6
        toappend = False

        if typeid == 4:
            value = ""
            while binstring[binpos] == "1":
                value += binstring[binpos+1:binpos+5]
                binpos += 5
                totalbits += 5

            value += binstring[binpos+1:binpos+5]
            stack[-1][3].append(int(value, 2))
            binpos += 5
            totalbits += 5
        else:
            lengthtype = binstring[binpos]
            binpos += 1
            totalbits += 1
            stackmodifier = 1

            if lengthtype == "0":
                subpacketbits = int(binstring[binpos:binpos+15],2)
                binpos += 15
                totalbits += 15
                toappend = ["b", subpacketbits, typeid, []]
            else:
                subpackets = int(binstring[binpos:binpos+11],2)
                binpos += 11
                totalbits += 11
                toappend = ["p", subpackets, typeid, []]

        for idx in range(len(stack)):
            if stack[idx][0] == "b":
                stack[idx][1] -= totalbits

        if stack[-1][0] == "p":
            stack[-1][1] -= 1

        if toappend:
            stack.append(toappend)

        while stack and stack[-1][1] == 0:
            if stack[-1][2] == 0:
                stack[-2][3].append(sum(stack[-1][3]))
            elif stack[-1][2] == 1:
                stack[-2][3].append(prod(stack[-1][3]))
            elif stack[-1][2] == 2:
                stack[-2][3].append(min(stack[-1][3]))
            elif stack[-1][2] == 3:
                stack[-2][3].append(max(stack[-1][3]))
            elif stack[-1][2] == 5:
                stack[-2][3].append(1 if stack[-1][3][0] > stack[-1][3][1] else 0)
            elif stack[-1][2] == 6:
                stack[-2][3].append(1 if stack[-1][3][0] < stack[-1][3][1] else 0)
            elif stack[-1][2] == 7:
                stack[-2][3].append(1 if stack[-1][3][0] == stack[-1][3][1] else 0)


            if stack[-1][0] == "s":
                print(stack[-1][3])
            stack.pop()


