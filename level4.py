
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
