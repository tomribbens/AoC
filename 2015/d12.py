#!/usr/bin/python3

# Day 12

from aocd import get_data
from queue import LifoQueue
import json



if __name__ == "__main__":
    data = get_data(year=2015, day=12)


    print("Part A:", end=" ")

    datajs = json.loads(data)

    stack = LifoQueue()
    stack.put(datajs)

    total = 0

    while stack.qsize() > 0:
        activeentry = stack.get()

        if isinstance(activeentry, int):
            total += activeentry
            continue

        if isinstance(activeentry, str) and activeentry.isnumeric():
            total += int(activeentry)
            continue

        if isinstance(activeentry, list):
            for entry in activeentry:
                stack.put(entry)
            continue

        if isinstance(activeentry, dict):
            for entry in activeentry.values():
                stack.put(entry)
            continue

        if isinstance(activeentry, str):
            continue
            

        print(type(activeentry))
        break

    print(total)


    
    print("Part B:", end=" ")
    
    stack = LifoQueue()
    stack.put(datajs)

    total = 0

    while stack.qsize() > 0:
        activeentry = stack.get()

        if isinstance(activeentry, int):
            total += activeentry
            continue

        if isinstance(activeentry, str) and activeentry.isnumeric():
            total += int(activeentry)
            continue

        if isinstance(activeentry, list):
            for entry in activeentry:
                stack.put(entry)
            continue

        if isinstance(activeentry, dict):
            if "red" in activeentry.values():
                continue
            for entry in activeentry.values():
                stack.put(entry)
            continue

        if isinstance(activeentry, str):
            continue
            

        print(type(activeentry))
        break

    print(total)
