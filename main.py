import math
import random

board = {}
for i in range(9):
    i = i+1
    board.update({i:' '})

def printBoard(board):
    i=1
    while i < 10:
        print(board[i]+"|",end=" ")
        if i%3 == 0:
            print("\n-------")
        i = i + 1
    print("\n")

def threestep(i,j,k,player,board):
    if board.get(i) == player and board.get(j) == player and board.get(k) == player:
        return 1
    else:
        return 0

def freeSpace(index):
    if board[index] == ' ':
        return True
    else:
        return False

def checkDiagonal(player,board):
    if threestep(1,5,9,player,board) or threestep(3,5,7,player,board):
        return 1
    else:
        return 0

def checkStraightH(player,board):
    if threestep(1,2,3,player,board) or threestep(4,5,6,player,board) or threestep(7,8,9,player,board):
        return 1
    else:
        return 0

def checkStraightV(player,board):
    if threestep(1,4,7,player,board) or threestep(2,5,8,player,board) or threestep(3,6,9,player,board):
        return 1
    else:
        return 0

def checkWin(player,board):
    if checkDiagonal(player,board) or checkStraightH(player,board) or checkStraightV(player,board):
        return 1
    else:
        return 0

def checkDraw(board):
    boardValues = board.values()
    if ' ' not in boardValues:
        return True
    else:
        return False

def computer_play(board):  #Dumb move using random
    box = random.choice(range(1,9))
    while(not freeSpace(box)):
        box = random.choice(range(1,9))
    insertValue('O',box)
            
def insertValue(player,index):
    if freeSpace(index):
        board[index] = player
        return
    else:
        index = int(input("Enter again:"))
        insertValue(player,index)
        return

if __name__ == "__main__":
    printBoard(board)
    while True:
        box = int(input("Enter the box position:"))
        insertValue('X',box)
        if checkWin('X',board):
            printBoard(board)
            print("player WON")
            break
        if checkDraw(board):
            print("Draw")
            break
        computer_play(board)
        printBoard(board)
        if checkWin('O',board):
            print("PC WON")
            break