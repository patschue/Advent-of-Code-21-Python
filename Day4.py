# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:18:56 2021

@author: schue
"""

# with open("InputDay4.txt") as f:
#     bingo = f.read().split("\n\n")
#     bingoZahl = bingo[0].split(",")
#     dictOfWords = []
secondBoard = [["x","x","x","x","x"],
                ["x","x","x","x","x"],
                ["x","x","x","x","x"],
                ["x","x","x","x","x"],
                ["x","x","x","x","x"]]
#     # for i in range(len(bingo)):
#     #     if i > 0:
#     #         bingoBoard.append(bingo[i].split())
#     bingoBoard = [bingo[i].splitlines() for i in range(len(bingo)) if i > 0]
#     bingoBoard = [bingo[x][y].split(" ") for x in bingoBoard for y in bingoBoard]
#     print(bingoBoard[0][0][1])
#     # bingoBoard = [bingo[i].splitlines() for i in range(len(bingo)) if i > 0]

# with open("InputDay4.txt") as f:
#     nums, *bingoBoard = f.read().split("\n\n")
#     bingoBoard = [[row.split() for row in bingoBoard.split("\n")] for bingoBoard in bingoBoard]
#     bingoZahl = nums.split(",")
#     # print(bingoBoard[0][0][1])
#     secondBoards = [secondBoard.copy() for i in bingoBoard]
#     Zahl = bingoZahl[0]
#     # for Zahl in bingoZahl:
#     for board in range(len(bingoBoard)):
#         for row in range(len(bingoBoard[board])):
#             for column in range(len(bingoBoard[board][row])):
#                 if int(bingoBoard[board][row][column]) == int(Zahl):
#                     print(board, row, column)
#                     secondBoards[board][row][column] = int(Zahl)
#                     print(Zahl)

def main():
    with open("InputDay4.txt") as input:
        print(part1(input))
    with open('InputDay4.txt') as input:
        print(part2(input))

def part1(input):
    randNums = []
    boards = []
    boardNum = 0
    boardData = {}
    boardLength = None

    for line in input:
        if len(randNums) == 0:
            for num in line.strip().split(','):
                randNums.append(int(num))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                boardNum += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if boardNum == len(boards):
                boards.append([])

            boards[boardNum].append([[int(num), 0] for num in line.split()])

    bingo = False
    bingoSum = 0
    for num in randNums:
        for board in boards:
            board = markNum(board, num)
            if checkBoard(board):
                bingo = True
                for row in board:
                    for x in row:
                        bingoSum += x[0] if x[1]==0 else 0
                return bingoSum*num


def markNum(board, n):
    for row in board:
        for num in row:
            if num[0] == n:
                num[1] = 1

    return board

def checkBoard(board):
    for row in board:
        sum = 0
        for num in row:
            sum += num[1]
        if sum == len(row):
            return True
    
    for i in range(len(board[0])):
        sum = 0
        for row in board:
            sum += row[i][1]
        if sum == len(board[0]):
            return True

def part2(input):
    randNums = []
    boards = []
    boardNum = 0
    boardData = {}
    boardLength = None

    for line in input:
        if len(randNums) == 0:
            for num in line.strip().split(','):
                randNums.append(int(num))
        else:
            if len(boards) == 0 and len(line.strip()) == 0:
                continue
            if len(line.strip()) == 0:
                boardNum += 1
                continue
            if boardLength is None:
                boardLength = len([i for i in line.split()])

            if boardNum == len(boards):
                boards.append([])

            boards[boardNum].append([[int(num), 0] for num in line.split()])


    bingo = False
    bingoNum = 0
    bingoSum = 0
    for num in randNums:
        for i in range(len(boards)-1, -1, -1):
            board = boards[i]
            board = markNum(board, num)
            if checkBoard(board):
                if len(boards) != 1:
                    boards.remove(board)
                else:
                    bingoNum = num
                    bingo = True
                    break
        if bingo:
            break

    sum =0
    for row in boards[0]:
        for num in row:
            bingoSum += num[0] if num[1]==0 else 0
    return bingoSum * bingoNum


if __name__=='__main__':
    main()