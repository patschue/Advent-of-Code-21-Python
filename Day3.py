# -*- coding: utf-8 -*-
"""
@author: Patrick

Thanks for the idea and hints with "filter(lambda" @ Jan Z.!
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
        
Partone()


with open("InputDay3.txt") as f:
    lstOX = f.read().split("\n")
    for x in range(len(lstOX[0])):
        Counter = 0
        if len(lstOX) >1:
            for y in lstOX:
                if int(y[x]) == 1:
                    Counter +=1
                else:
                    Counter -=1
            if Counter < 0:
                lstOX = list(filter(lambda z: z[x] == "0", [z for z in lstOX]))
            else:
                lstOX = list(filter(lambda z: z[x] == "1", [z for z in lstOX]))



with open("InputDay3.txt") as f:
    lstCO = f.read().split("\n")
    for x in range(len(lstCO[0])):
        Counter = 0
        if len(lstCO) >1:
            for y in lstCO:
                if int(y[x]) == 1:
                    Counter +=1
                else:
                    Counter -=1
            if Counter >= 0:
                lstCO = list(filter(lambda z: z[x] == "0", [z for z in lstCO]))
            else:
                lstCO = list(filter(lambda z: z[x] == "1", [z for z in lstCO]))
    OXvalue = int("111010111111", 2)
    COvalue = int("010010000111", 2)
    print(OXvalue * COvalue)