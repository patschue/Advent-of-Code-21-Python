# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:55:16 2021

@author: schue
"""

# CheckMiddle(value, row, point):
    

with open("InputDay9.txt") as f:
    ground = f.read().splitlines()
    ground = [list(ground[x]) for x in range(len(ground))]
    ground = [[int(x) for x in ground[row]] for row in range(len(ground))]
    resultlist = []
    result = 0

    # first corner
    if ground[0][0] < ground[0][1] and ground[0][0] < ground[1][0]:
        resultlist.append(ground[0][0])
    # second corner
    if ground[0][-1] < ground[0][-2] and ground[0][-1] < ground[1][-1]:
        resultlist.append(ground[0][-1])
    # third corner
    if ground[-1][-1] < ground[-1][-2] and ground[-1][-1] < ground[-2][-1]:
        resultlist.append(ground[-1][-1])
    # fourth corner
    if ground[-1][0] < ground[-1][1] and ground[-1][0] < ground[-2][0]:
        resultlist.append(ground[-1][0])
        
    # first row
    for i in range(1, len(ground[0])-1):
        if ground[0][i] < ground[0][i-1] and ground[0][i] < ground[0][i+1] and ground[0][i] < ground[1][i]:
            resultlist.append(ground[0][i])           
    # last row
    for i in range(1, len(ground[0])-1):
        if ground[-1][i] < ground[-1][i-1] and ground[-1][i] < ground[-1][i+1] and ground[-1][i] < ground[-2][i]:
            resultlist.append(ground[-1][i])  
    # first column
    for i in range(1, len(ground)-1):
        if ground[i][0] < ground[i-1][0] and ground[i][0] < ground[i+1][0] and ground[i][0] < ground[i][1]:
            resultlist.append(ground[i][0])  
    # last column
    for i in range(1, len(ground)-1):
        if ground[i][-1] < ground[i-1][-1] and ground[i][-1] < ground[i+1][-1] and ground[i][-1] < ground[i][-2]:
            resultlist.append(ground[i][-1])
    
    for row in range(1, len(ground)-1):
        for column in range(1, len(ground[0])-1):
            if ground[row][column] < ground[row][column-1] and ground[row][column] < ground[row][column+1] and ground[row][column] < ground[row-1][column] and ground[row][column] < ground[row+1][column]:
                resultlist.append(ground[row][column])
                
print(sum(resultlist) + len(resultlist))