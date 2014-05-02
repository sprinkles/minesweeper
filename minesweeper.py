#!/usr/bin/python3
#level6
#minesweeper.py

from game import *
from gameio import *

def playGame(sboard,mboard): 
    print('Here we go!')
    displayBoard(sboard)
    #while(move(sboard,mboard)==0):
    while True:
        mv=move(sboard,mboard)
        if mv==2:
            print("You may have won.")
            break
        elif mv==1:
            print("You lose.")
            break
        else:
            continue
        
    
def main():
    
    #rows = int(sys.argv[1]) if len(sys.argv) >=2 else 9
    #cols = int(sys.argv[2]) if len(sys.argv) >=3 else 9
    #bombs= int(sys.argv[3]) if len(sys.argv) >=4 else 10
    rows = 9
    cols = 9
    bombs = 10
    
    #allocate boards
    sboard=createBoard(rows,cols)
    sboard=initBoard(sboard)
    
    mboard=createBoard(rows,cols)
    mboard=initBoard(mboard)
    
    mines = placeBombs(bombs,mboard)
    #displayBoard(mboard)
    mboard = placeBombCount(mboard)
    #displayBoard(mboard)
    
    #playgame loop
    playGame(sboard,mboard)


main()
