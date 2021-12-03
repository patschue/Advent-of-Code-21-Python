# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:04:53 2021

@author: schue
"""

def Partone():
    with open("InputDay3.txt") as f:
        line = f.readline().strip()
        countercolumn = 0
        gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while line:
            for i in line:
                if int(i) == 1:
                    gamma[countercolumn] += 1
                    epsilon[countercolumn] -= 1
                else:
                    gamma[countercolumn] -= 1
                    epsilon[countercolumn] += 1
                countercolumn += 1
            line = f.readline().strip()
            countercolumn = 0
        gammavalue = int("101000101001", 2)
        epsilonvalue = int("010111010110", 2)
        print(gammavalue * epsilonvalue)
        
# Partone()

with open("InputDay3.txt") as f:
    # lst = [int(val) for val in f.readline().split()]
    lst = f.read().split()
    # print(type(lst[0]))
    Counter = 0
    for i in range(len(lst)):
        if int(lst[i][0]) == 1:
            Counter +=1
        else:
            Counter -=1
    if Counter >= 0:
        # print("Test")
        for x in range(len(lst)):
            if int(lst[x][0]) == 0:
                del lst[x]
        # newlst = [lst.remove(x) for x in lst if int(lst[x][0]) == 0]
    else:
        for x in range(len(lst)):
            if int(lst[x][0]) == 1:
                del lst[x]
        # newlst = [lst.remove(x) for x in lst if int(lst[x][0]) == 1]
