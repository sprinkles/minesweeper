#level2.py
#At the start, this procedure should just print the word BOOM.
from game import *
from gameio import *

rows=9
cols=9
bombs=10

sboard=createBoard(rows,cols)
sboard=initBoard(sboard)

mboard=createBoard(rows,cols)
mines = placeBombs(bombs,mboard)
mboard = placeBombCount(mboard)
#displayBoard(mboard)
displayBoard(sboard)

cnt=3
while(cnt):
    mv=move(sboard,mboard)
    cnt-=1

displayBoard(sboard)
goBoom()
goBoomBigger()
