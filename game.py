#!/usr/bin/python
import random
import sys

def createBoard(rows,cols):
    return [[]*cols for i in range(rows) 

def initBoard(board):
    rows = len(board)
    cols = len(board[0])
    return [['-']*cols for i in range(rows) 

#level0
def placeBombs(bombs,board):                                                            
    rows = len(board)                                                                   
    cols = len(board[0])                                                                
    mines=[]                                                                             
    while(bombs):                                                                       
        randr = random.randint(0,rows-1) 
        randc = random.randint(0,cols-1)                                                  
        if (randr,randc) not in mines:                                                                 
            board[randr][randc]='B'
            mines.append((randr,randc))
            #print(mines)
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
            board[r][c]=calcAdj(board,(r,c))
    #return board[calcAdj(mboard,loc(r,c)) for c in range(cols) for r in range(rows)]
    return board
    
#level4.py
#endOfGame(sboard,mboard): 0 if only mines left, else 1
def endOfGame(sboard,mboard):
    """Returns 0 if only mines are left to uncover"""
    if '-' not in [x for row in sboard for x in row]:
        return 0
    else: 
        return 1

