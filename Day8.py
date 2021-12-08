# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 06:48:37 2021

@author: schue
"""

with open("InputDay8.txt") as f:
    inputs = f.read().splitlines()
    search = [2, 4, 3, 7]
    inputs = [inputs[x].split("|") for x in range(len(inputs))]
    output = [inputs[x][1].split() for x in range(len(inputs))]
    result = 0
    for line in output:
        tempresult = 0
        print(line)
        for i in range(len(line)):
            if len(line[i]) in search:
                tempresult += 1
        result += tempresult
    print("Part 1:", result)



# def CheckNo(signal):
#     for i in range(len(search)):
#         if sorted(signal) == sorted(search[i]):
#             return i


# with open("InputDay8.txt") as f:
#     inputs = f.read().splitlines()
#     search = ["cagedb", "ab", "gcdfa", "fbcad", "eafb", "cdfbe", "cdfgeb", "dab", "acedgfb", "cefabd"]
#     inputs = [inputs[x].split("|") for x in range(len(inputs))]
#     output = [inputs[x][1].split() for x in range(len(inputs))]
#     result = 0
#     for line in output:
#         tempresult = []
#         for word in range(len(line)):
#             tempresult.append(CheckNo(line[word]))

#             # tempresult = tempresult.join
#             # tempresult += (CheckNo(line[word]))
#             # print(CheckNo(line[i]))
#         tempresult = [str(i) for i in tempresult]
#         tempresult = int("".join(tempresult))
        result += tempresult
