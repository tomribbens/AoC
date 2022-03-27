#!/usr/bin/python3

# Day 10

from aocd import get_data

def validpw(pwarr):
    banned = [ord("i"), ord("o"), ord("l")]
    if any(x in pwarr for x in banned):
        return False

    pairs = 0
    straight = False
    skip = False
    for idx, val in enumerate(pwarr):
        if skip:
            skip = False
            continue

        if idx == 0:
            continue

        if val == pwarr[idx-1]:
            pairs += 1
            skip = True
            continue

        if not straight and idx >= 2:
            if pwarr[idx-2] == val - 2 and pwarr[idx-1] == val - 1:
                straight = True
    

    if pairs < 2:
        return False

    if not straight: 
        return False

    return True

def nextpw(pw):
    pwarr = [ord(c) for c in pw]
    
    while True:
        pwarr[-1] += 1
        carry = 0
        for idx, val in reversed(list(enumerate(pwarr))):
            if carry:
                val += carry
                carry = 0
            if val > ord("z"):
                val = val - 26
                carry = 1

            pwarr[idx] = val

        if validpw(pwarr):
            break

    return ''.join(chr(i) for i in pwarr)



if __name__ == "__main__":
    line = get_data(year=2015, day=11).splitlines()[0]


    print("Part A:", end=" ")
    answera = nextpw(line)
    print(answera)

    
    print("Part B:", end=" ")
    answerb = nextpw(answera)
    print(answerb)
    
