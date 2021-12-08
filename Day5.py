# -*- coding: utf-8 -*-
"""
@author: Patrick
Part one working
"""

with open("InputDay5.txt") as f:
    Matrix = f.read().splitlines()
    Matrix = [Matrix[i].split(" -> ") for i in range(len(Matrix))]
    Matrix = [[Matrix[i][y].split(",") for y in range(len(Matrix[i]))] for i in range(len(Matrix))]
    Result = {}
    for i in range(len(Matrix)):
        x1 = int(Matrix[i][0][0])
        x2 = int(Matrix[i][1][0])
        y1 = int(Matrix[i][0][1])
        y2 = int(Matrix[i][1][1])
        minx = min(x1, x2)
        miny = min(y1, y2)
        if x1 == x2:
            diff = y2 - y1
            for i in range(abs(diff)+1):
                Result[x1, miny+i] = Result.get((x1, miny+i), 0) + 1
        if y1 == y2:
            diff = x2 - x1
            for i in range(abs(diff) + 1):
                Result[minx+i, y1] = Result.get((minx+i, y1), 0) + 1
    fertig = sum(1 for x in Result.values() if x > 1)
        