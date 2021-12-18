#!/usr/bin/python3

# Day 16, part 1 of Advent of Code 2021

import sys

class Snailfishnr:
    def __init__(self, *args):
        if isinstance(args[0], (list, int)) and isinstance(args[1], (list, int)):
            self.initfromnrs(*args)
        elif isinstance(args[0], str):
            self.initfromstr(*args)
        else:
            raise TypeError


    def initfromnrs(self, p1, p2, depth=0):
        self.depth = depth
        if isinstance(p1, int):
            self.p1 = p1
        elif isinstance(p1, list):
            if len(p1) != 2:
                raise ValueError
            self.p1 = Snailfishnr(*p1, self.depth + 1)
            
        if isinstance(p2, int):
            self.p2 = p2
        elif isinstance(p2, list):
            if len(p2) != 2:
                raise ValueError
            self.p2 = Snailfishnr(*p2, self.depth + 1)

    def initfromstr(self, x, depth=0):
        self.depth = depth
        if x[0] != "[" and x[-1] != "]":
            raise ValueError

        x = x[1:-1]
        
        if x[0] != "[":
            parts = x.split(",", 1)
            self.p1 = int(parts[0])

            if parts[1][0] != "[":
                self.p2 = int(parts[1])
            else:
                self.p2 = Snailfishnr(parts[1], self.depth + 1)
        else:
            idx = 0
            bracketsdepth = 1
            while bracketsdepth > 0:
                idx += 1
                if x[idx] == "[":
                    bracketsdepth += 1
                elif x[idx] == "]":
                    bracketsdepth -= 1

            self.p1 = Snailfishnr(x[0:idx+1], self.depth + 1)

            if x[idx+2] == "[":
                self.p2 = Snailfishnr(x[idx+2:], self.depth + 1)
            else:
                self.p2 = int(x[idx+2:])

    def __repr__(self):
        return "[" + repr(self.p1) + "," + repr(self.p2) + "]"

    def maxdepth(self):
        tmp = self.depth
        if isinstance(self.p1, Snailfishnr):
            tmp = max(tmp, self.p1.maxdepth())

        if isinstance(self.p2, Snailfishnr):
            tmp = max(tmp, self.p2.maxdepth())

        return tmp

    def addleft(self, toadd):
        if isinstance(self.p1, int):
            self.p1 += toadd
            return
        
        self.p1.addleft(toadd)
        return

    def addright(self, toadd):
        if isinstance(self.p2, int):
            self.p2 += toadd
            return
        
        self.p2.addright(toadd)
        return

    def explode(self):
        exploding = False
        if self.maxdepth() < 4:
            return False
        
        if self.depth == 4:
            return (self.p1, self.p2)
        
        if isinstance(self.p1, Snailfishnr):
            exploding = self.p1.explode()
        
        if exploding:
            if self.depth == 3:
                self.p1 = 0
            if isinstance(self.p2, int):
                self.p2 += exploding[1]
            else:
                self.p2.addleft(exploding[1])
            return (exploding[0], 0)

        if isinstance(self.p2, Snailfishnr):
            exploding = self.p2.explode()
        
        if exploding:
            if self.depth == 3:
                self.p2 = 0
            if isinstance(self.p1, int):
                self.p1 += exploding[0]
            else:
                self.p1.addright(exploding[0])
            return (0, exploding[1])

    def split(self):
        issplit = False
        if isinstance(self.p1, int):
            if self.p1 >= 10:
                self.p1 = Snailfishnr(int(self.p1/2), int(self.p1/2+self.p1%2), self.depth + 1)
                return True
        else:
            issplit = self.p1.split()

        if not issplit:
            if isinstance(self.p2, int):
                if self.p2 >= 10:
                    self.p2 = Snailfishnr(int(self.p2/2), int(self.p2/2+self.p2%2), self.depth + 1)
                    return True
            else:
                issplit = self.p2.split()

        return issplit
        

    def reduce(self):
        while self.explode() or self.split():
            continue
    


    def __add__(self, o):
        sumof = Snailfishnr("[" + repr(self) + "," + repr(o) + "]")
        sumof.reduce()
        return sumof

    def magnitude(self):
        total = 0
        if isinstance(self.p1, int):
            total += 3 * self.p1
        else:
            total += 3 * self.p1.magnitude()

        
        if isinstance(self.p2, int):
            total += 2 * self.p2
        else:
            total += 2 * self.p2.magnitude()

        return total

            
        

with open(str(sys.argv[1])) as input_file:
    numbers = [Snailfishnr(line.strip()) for line in input_file]

maxmagnitude = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i == j:
            continue

        result = numbers[i] + numbers[j]
        if maxmagnitude < result.magnitude():
            maxmagnitude = result.magnitude()

print(maxmagnitude)
