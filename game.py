#!/usr/bin/python3

import random
import sys

def createBoard(rows,cols):
    return [['0']*cols for i in range(rows)]

def initBoard(board):
    rows = len(board)
    cols = len(board[0])
    return [['-']*cols for i in range(rows)]

#level0
def placeBombs(bombs,board): 
    rows = len(board)  
    cols = len(board[0])
    print(rows,cols)
    mines=[]
    while(bombs):
        randr = random.randint(0,rows-1)
        randc = random.randint(0,cols-1) 
        if (randr,randc) not in mines: 
            board[randr][randc]='B'
            mines.append((randr,randc))
            bombs-=1
    return mines

#level0
def calcAdj(board,loc):
    row = loc[0]   
    col = loc[1]
    total=0
    for r in range(row-1,row+2):
        if r<0: continue
        for c in range(col-1,col+2):
            if c<0: continue
            try:
                board[r][c]
            except IndexError:
                continue
            else:
                total+=1 if board[r][c] == 'B' else 0 
    return total   

#level1, but really level0
def displayBoard(board):
    """Prints the board with indices"""
    rows = len(board)
    cols = len(board[0])
    for r in range(-1,rows):
        for c in range(-1,cols):
            if r==c==-1:
                print(end="   ")
            print(str(c) if r==-1 and c>-1 else '',end=" ")
            print(str(r) if c==-1 and r>-1 else '',end=" ")
            if r>-1 and c>-1:
                print(board[r][c], end="")
        print()                                               
    return 

#level0
def placeBombCount(board):
    rows = len(board) 
    cols = len(board[0])
    for r in range(0,rows):
        for c in range(0,cols):
            if board[r][c] != 'B':
                board[r][c]=calcAdj(board,(r,c))
    return board
    
#level4
# endOfGame(sboard,mboard): 0 if only mines left, else 1
# (I'm following a set of requirements) 
def endOfGame(sboard,mboard):
    """Returns 0 if only mines are left to uncover"""
    if '-' not in [x for row in sboard for x in row]:
        return 0
    else: 
        return 1

def getNeighbors(board,loc):
    row = loc[0]
    col = loc[1]
    rows=len(board)
    cols=len(board[0])
    
    neighbors = []
 
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 and j == 0: continue
            elif -1<row+i<rows and -1<col+j<cols:
                neighbors.append((row+i,col+j))
    return neighbors

#level3
def showCell(sboard,mboard,loc):
    """Returns 1 if bomb, 0 if not"""
    r=loc[0]
    c=loc[1]
    #check endOfGame
    if(sboard[r][c] != '-'):
        return 0
    
    if(mboard[r][c] == 'B'):
        return 1
    
    sboard[r][c] = mboard[r][c]
    
    if(sboard[r][c] == 0):
        for rr,cc in getNeighbors(sboard,(r,c)):
            showCell(sboard,mboard,[rr,cc])


