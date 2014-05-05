#level1.py
# displayBoard(sboard,mboard)
# compare sboard(loc)=mboard(loc)

from game import *
from gameio import *

rows=9
cols=9
bombs=10

sboard=createBoard(rows,cols)
sboard=initBoard(sboard)

mboard=createBoard(rows,cols)
mines = placeBombs(bombs,mboard)
displayBoard(mboard)


