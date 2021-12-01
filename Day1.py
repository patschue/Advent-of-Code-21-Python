# -*- coding: utf-8 -*-
"""
@author: Patrick
"""        
    
def CounterDay1(liste):
    result = 0
    for i in range(len(liste)):
        if liste[i] > liste[i-1]:
            result += 1
    return result

####################################

with open("InputDay1.txt") as f:
    lst = [int(x) for x in f.read().split()]
    print("Result of part 1:", CounterDay1(lst))

####################################################

with open("InputDay1.txt") as f:
    lstTemp = []
    lst = f.read().split()
    überzählig = len(lst) % 3
    for i in range(len(lst) - überzählig):
        lstTemp.append(int(lst[i]) + int(lst[i+1]) + int(lst[i+ 2]))
    print("Result of part 2:", CounterDay1(lstTemp))

