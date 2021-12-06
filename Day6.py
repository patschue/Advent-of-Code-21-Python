# -*- coding: utf-8 -*-
"""
@author: Patrick

"""

with open("InputDay6.txt") as f:
    latfish = f.read().split(",")
    latfish = [int(x) for x in latfish]
    for i in range(80):
        for x in range(len(latfish)):
            if latfish[x] != 0:
                latfish[x] -= 1
            else:
                latfish[x] = 6
                latfish.append(8)
    print("Part 1:", len(latfish))


with open("InputDay6.txt") as f:
    latfish = f.read().split(",")
    latfish = [int(x) for x in latfish]
    ages = [0,0,0,0,0,0,0,0,0]
    noIteratrions = 256  
    for fishes in latfish:
        ages[fishes] += 1
    for i in range(noIteratrions):
        tempReset = ages[0]
        ages += [ages.pop(0)]
        ages[6] += tempReset
        ages[8] = tempReset
    print("Part 2:", sum([x for x in ages]))
