#level0.py
## createBoard(rows,cols): returns empty matrix?
## initBoard(sboard): returns covered matrix
## placeBombs(mboard,bombs): returns mines[] and places 'B's on mboard
## checkAdj(mboard,loc): returns total adj
## placeBombCount(mboard,loc) via checkAdj

from game import *
from gameio import *

rows=9
cols=9
bombs=10

sboard=createBoard(rows,cols)
print('sboard is here!')
displayBoard(sboard)

sboard=initBoard(sboard)
print('sboard is covered!')
displayBoard(sboard)

mboard=createBoard(rows,cols)
print('mboard is here!')
displayBoard(mboard)
    
mines = placeBombs(bombs,mboard)
print('mboard has bombs!')
displayBoard(mboard)

mboard = placeBombCount(mboard)
print('mboard has bomb counts!')
displayBoard(mboard)


