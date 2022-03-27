#!/usr/bin/python3

# Day 5

from aocd import lines
import re
import numpy as np

class Lights:
    def __init__(self, size):
        self.lights = np.full((size, size), False)


    def turnOn(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = True

    def turnOff(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = False

    def toggle(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] = np.invert(self.lights[start[0]:end[0]+1, start[1]:end[1]+1])

    def onLights(self):
        return self.lights.sum()

class BLights:
    def __init__(self, size):
        self.lights = np.zeros((size, size), dtype=np.int64)


    def turnOn(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] += 1

    def turnOff(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] -= 1
        self.lights[self.lights<0] = 0

    def toggle(self, start, end):
        # start and end are tuples of x,y coordinates
        self.lights[start[0]:end[0]+1, start[1]:end[1]+1] += 2

    def onLights(self):
        return self.lights.sum()

def parseLine(line, lights):
    action, startx, starty, endx, endy = re.match(r"(.*) (\d+),(\d+) through (\d+),(\d+)", line).groups()
    start = (int(startx), int(starty))
    end = (int(endx), int(endy))
    if action == "toggle":
        lights.toggle(start, end)
    elif action == "turn on":
        lights.turnOn(start, end)
    elif action == "turn off":
        lights.turnOff(start, end)
        


if __name__ == "__main__":

    mylights = Lights(1000)
    for line in lines:
        parseLine(line, mylights)
    print("Part A:", end=" ")
    print(mylights.onLights())


    myBlights = BLights(1000)
    for line in lines:
        parseLine(line, myBlights)
    print("Part B:", end=" ")
    print(myBlights.onLights())
    
