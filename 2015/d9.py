#!/usr/bin/python3

# Day 9

from aocd import get_data
from itertools import permutations
import networkx as nx
import re


if __name__ == "__main__":
    lines = get_data(year=2015, day=9).splitlines()

    G = nx.Graph()
    locations = set()

    for line in lines:
        start, end, distance = re.match(r"(\w+) to (\w+) = (\d+)", line).groups()
        distance = int(distance)
        G.add_edge(start, end, weight=distance)
        locations.add(start)
        locations.add(end)





    print("Part A:", end=" ")
    print(min(nx.path_weight(G, path , weight='weight') for path in permutations(locations)))

    
    print("Part B:", end=" ")
    print(max(nx.path_weight(G, path , weight='weight') for path in permutations(locations)))

