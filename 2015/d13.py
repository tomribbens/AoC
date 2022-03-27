#!/usr/bin/python3

# Day 13

from aocd import get_data
from itertools import permutations
import networkx as nx
import re


if __name__ == "__main__":
    lines = get_data(year=2015, day=13).splitlines()

    G = nx.Graph()
    people = set()

    for line in lines:
        p1, sign, happy, p2 = re.match(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line).groups()
        happy = int(happy) * (-1 if sign == "lose" else 1)
        if G.has_edge(p1, p2):
            G[p1][p2]['weight'] += happy
        else:
            G.add_edge(p1, p2, weight=happy)

        people.add(p1)
        people.add(p2)





    print("Part A:", end=" ")
    print(max(nx.path_weight(G, path + path[0:1], weight='weight') for path in permutations(people)))

    
    print("Part B:", end=" ")
    for person in people:
        G.add_edge(person, "me", weight=0)
    people.add("me")
    print(max(nx.path_weight(G, path + path[0:1], weight='weight') for path in permutations(people)))
