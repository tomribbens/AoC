#!/usr/bin/python3

# Day 12, part 1 of Advent of Code 2021

import sys
import copy

def paths(graph, pos, visited, fullvisited):
    if pos == "end":
        newfullvisited = copy.deepcopy(fullvisited)
        newfullvisited.append(pos)
        # Uncomment if you want all full paths printed:
        # print(newfullvisited)
        return 1
    else:
        if "secondtime" not in visited and pos not in visited:
            options = [i for i in graph[pos] if i != "start"]
        else:
            options = [i for i in graph[pos] if i not in visited and i != "start"] 
        newVisited = copy.deepcopy(visited)
        newfullvisited = copy.deepcopy(fullvisited)
        if pos in visited:
            newVisited.append("secondtime")
        if pos.islower() and pos != "start":
            newVisited.append(pos)

        newfullvisited.append(pos)


        pathways = 0
        for option in options:
            pathways += paths(graph, option, newVisited, newfullvisited)

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

print(paths(graph, "start", [], []))
