#!/usr/bin/python3

# Day 7

from aocd import get_data
from queue import LifoQueue
import re


class Circuit:
    def __init__(self, lines):
        self.gates = {}

        for line in lines:
            value, key = line.split(" -> ")
            if value.isnumeric():
                value = int(value)

            self.gates[key] = value


    def Solve(self, key):
        stack = LifoQueue()
        stack.put(key)

        while stack.qsize() > 0:
            activekey = stack.get()

            if isinstance(self.gates[activekey], int):
                continue

            op1, action, op2 = re.match(r"([a-z0-9]+)? ?([A-Z]+)? ?([a-z0-9]+)?", self.gates[activekey]).groups("")

            if not op1 == "" and not op1.isnumeric() and not isinstance(self.gates[op1], int):
                stack.put(activekey)
                stack.put(op1)
                continue

            if not op2 == "" and not op2.isnumeric() and not isinstance(self.gates[op2], int):
                stack.put(activekey)
                stack.put(op2)
                continue

            if action == "":
                self.gates[activekey] = int(op1) if op1.isnumeric() else self.gates[op1]
            elif action == "LSHIFT":
                self.gates[activekey] = (int(op1) if op1.isnumeric() else self.gates[op1]) << (int(op2) if op2.isnumeric() else self.gates[op2])
            elif action == "RSHIFT":
                self.gates[activekey] = (int(op1) if op1.isnumeric() else self.gates[op1]) >> (int(op2) if op2.isnumeric() else self.gates[op2])
            elif action == "NOT":
                self.gates[activekey] = (int(op2) if op2.isnumeric() else self.gates[op2]) ^ 65535
            elif action == "AND":
                self.gates[activekey] = (int(op1) if op1.isnumeric() else self.gates[op1]) & (int(op2) if op2.isnumeric() else self.gates[op2])
            elif action == "OR":
                self.gates[activekey] = (int(op1) if op1.isnumeric() else self.gates[op1]) | (int(op2) if op2.isnumeric() else self.gates[op2])

        return self.gates[key]
                    

    def setWire(self, key, value):
        self.gates[key] = value



if __name__ == "__main__":
    print("Part A:", end=" ")

    lines = get_data(year=2015, day=7).splitlines()
    myCircuit = Circuit(lines)
    partA = myCircuit.Solve("a")
    print(partA)


    print("Part B:", end=" ")
    myBCircuit = Circuit(lines)
    myBCircuit.setWire("b", partA)
    partB = myBCircuit.Solve("a")
    print(partB)
    
