#!/usr/bin/python3

# Day 12, part 1 of Advent of Code 2021

import sys
import copy

def paths(graph, pos, visited):
    if pos == "end":
        return 1
    else:
        options = [i for i in graph[pos] if i not in visited] 
        newVisited = copy.deepcopy(visited)
        if pos.islower():
            newVisited.append(pos)

        pathways = 0
        for option in options:
            pathways += paths(graph, option, newVisited)

        return pathways

            



graph = {}
with open(str(sys.argv[1])) as input_file:
    for line in input_file:
        x, y = line.strip().split("-")
        if x not in graph:
            graph[x] = []
        graph[x].append(y)
        if y not in graph:
            graph[y] = []
        graph[y].append(x)

print(paths(graph, "start", []))
