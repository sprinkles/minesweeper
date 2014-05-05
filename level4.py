# Level 4
# Define a "end of game" checking function that, when given a mine board and a status board, returns 0 if all covered squares contain mines and 1 otherwise.
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
print('End of game?',endOfGame(sboard,mboard))
print('Uncovering...')
sboard=uncoverBoard(sboard,mboard)
displayBoard(sboard)
print('End of game?',endOfGame(sboard,mboard))
