#!/usr/bin/python3

# Day 16, part 1 of Advent of Code 2021

import sys
import binascii

input_array = []
with open(str(sys.argv[1])) as input_file:
    input_array = [line.strip() for line in input_file]


for line in input_array:
    binstring = ''.join([format(int(x, 16), '04b') for x in line])


    stack = [["s", 0]]
    binpos = 0
    totalversion = 0
    while stack:
        version = int(binstring[binpos:binpos+3], 2)
        totalversion += version
        binpos += 3
        typeid = binstring[binpos:binpos+3]
        binpos += 3
        totalbits = 6
        toappend = False

        if typeid == "100":
            while binstring[binpos] == "1":
                binpos += 5
                totalbits += 5

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
                toappend = ["b", subpacketbits]
            else:
                subpackets = int(binstring[binpos:binpos+11],2)
                binpos += 11
                totalbits += 11
                toappend = ["p", subpackets]

        for idx in range(len(stack)):
            if stack[idx][0] == "b":
                stack[idx][1] -= totalbits

        if stack[-1][0] == "p":
            stack[-1][1] -= 1

        if toappend:
            stack.append(toappend)

        while stack and stack[-1][1] == 0:
            stack.pop()


    print(totalversion)






