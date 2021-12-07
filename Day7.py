# -*- coding: utf-8 -*-
"""
@author: Patrick
"""

with open("InputDay7.txt") as f:
    crabswarm = f.read().split(",")
    crabswarm = [int(x) for x in crabswarm]
    diff = {}
    diff = []
    maxno = max(crabswarm)
    minno = min(crabswarm)
    for i in range(minno, maxno):
        temp = 0
        for crab in crabswarm:
            temp += abs(crab - i)
        diff.append(temp)
    print("Part 1:", min(diff))


def Differenz(maximum):
    result = 0
    for i in range(0, maximum+1):
        result += i
    return result
        
# Part 2 is slow, takes a few minutes

# with open("InputDay7.txt") as f:
#     crabswarm = f.read().split(",")
#     crabswarm = [int(x) for x in crabswarm]
#     diff = {}
#     diff = []
#     maxno = max(crabswarm)
#     minno = min(crabswarm)
#     for i in range(minno, maxno):
#         temp = 0
#         for crab in crabswarm:
#             temp += Differenz(abs(crab - i))
#         diff.append(temp)
#     print("Part 2:", min(diff))