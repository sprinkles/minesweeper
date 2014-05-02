# Level 4
# Define a "end of game" checking function that, when given a mine board and a status board, returns 0 if all covered squares contain mines and 1 otherwise.
import game
import gameio

rows=5
cols=9
bombs=10

#rows  = argv[1]
#cols  = argv[2]
#bombs = argv[3]


sboard=createBoard(rows,cols)
sboard=initBoard(sboard)

mboard=createBoard(rows,cols)
mines = placeBombs(bombs,mboard)
mboard = placeBombCount(mboard)
#displayBoard(mboard)

displayBoard(sboard)
