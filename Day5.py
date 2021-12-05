# -*- coding: utf-8 -*-
"""
@author: Patrick
"""

# Sum is not working yet, ideas are welcome!

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
            Result[x1, miny] = Result.get("x1, miny", 0) + 1
            for i in range(abs(diff)):
                Result[x1, miny+i+1] = Result.get("x1, miny+i+1", 0) + 1
        if y1 == y2:
            diff = x2 - x1
            Result[minx, y1] = Result.get("minx, x2", 0) + 1
            if Result.get("minx, y1") == 1:
                print("Hello")
            else:
                print(Result.get("minx, y1"))
            for i in range(abs(diff)):
                Result[minx+i+1, y1] = Result.get("minx+i+1, y1", 0) + 1
        # print(Result)
        
        
# 0,9 -> 5,9
# 0,9 -> 2,9





###################
# Idea with numpy
###################



# import numpy as np

# with open("InputDay5.txt") as f:
#     Matrix = f.read().splitlines()
#     Matrix = [Matrix[i].split(" -> ") for i in range(len(Matrix))]
#     Matrix = [[Matrix[i][y].split(",") for y in range(len(Matrix[i]))] for i in range(len(Matrix))]
#     Result = np.zeros((1000, 1000))
#     Counter = 0
#     for i in range(len(Matrix)):
#         x1 = int(Matrix[i][0][0])
#         x2 = int(Matrix[i][1][0])
#         y1 = int(Matrix[i][0][1])
#         y2 = int(Matrix[i][1][1])
#         minx = min(x1, x2)
#         miny = min(y1, y2)
#         if x1 == x2:
#             diff = y2 - y1
#             Result[x1, miny] += 1
#             for i in range(abs(diff)):
#                 Result[x1, miny+i+1] += 1
#         if y1 == y2:
#             diff = x2 - x1
#             Result[minx, y1] += 1
#             for i in range(abs(diff)):
#                 Result[minx+i+1, y1] += 1
    # for i in range(len(Result)):
    #     print(i)
    #     for y in range(len(Result[i])):
    #         if Result[i][y] > 1:
    #             Counter += 1





###################
# Idea from reddit
###################




# with open("InputDay5.txt") as f:
#     Matrix = f.read().splitlines()
#     Matrix = [Matrix[i].split(" -> ") for i in range(len(Matrix))]
#     data = [[Matrix[i][y].split(",") for y in range(len(Matrix[i]))] for i in range(len(Matrix))]


# from typing import List

# def findall_as_ints(lines:str)->List[int]:
#     """Findall int in a string, returns as int"""
#     from re import findall
#     return [int(x) for x in findall('\d+', lines)]


# Result = np.zeros((1000, 1000))


# for i in data:
#     (x1, y1, x2, y2) = findall_as_ints(i)
#     minx = min(x1, x2)
#     maxx = max(x1, x2)
#     miny = min(y1, y2)
#     maxy = max(y1, y2)
#     if x1 == x2:
#         ymin = min(y1, y2)
#         ymax = max(y1, y2)
#         Result[ymin:ymax+1, x1] += 1
#     elif y1 == y2:
#         xmin = min(x1, x2)
#         xmax = max(x1, x2)
#         Result[y1, xmin:xmax+1] +=1
# print("Solution = ", Result[Result > 1].shape)