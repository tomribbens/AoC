#!/usr/bin/python3

# Day 14

from aocd import get_data
import operator
import re

def distance_flown(racetime, speed, endurance, resttime):
    cycles, remainder = divmod(racetime, endurance + resttime)
    distance = (speed * endurance) * cycles + speed * (remainder if remainder < endurance else endurance)

    return distance



if __name__ == "__main__":
    lines = get_data(year=2015, day=14).splitlines()
    reindeirdict = dict()

    for line in lines:
        reindeir, speed, endurance, resttime = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line).groups()
        speed = int(speed)
        endurance = int(endurance)
        resttime = int(resttime)
        reindeirdict[reindeir] = [speed, endurance, resttime]

    print("Part A:", end=" ")
    print(max(distance_flown(2503, *reindeirdict[reindeir]) for reindeir in reindeirdict.keys()))


    
    print("Part B:", end=" ")
    points = dict()
    for reindeir in reindeirdict.keys():
        points[reindeir] = 0

    for seconds in range(1, 2504):
        distances = {reindeir:distance_flown(seconds, *reindeirdict[reindeir]) for reindeir in reindeirdict.keys()}
        winningdistance = max(distances.values())
        winners = [r for r,d in distances.items() if d == winningdistance]
        for w in winners:
            points[w] += 1

        

    print(max(points.values()))
