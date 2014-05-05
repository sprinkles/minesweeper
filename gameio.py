#---
# file:gameio.py
# level:2
#---

from game import *

def goBoom():
    boomstring = """\
    .  xxxx     xxx    xxx    x     x   xx
    .  xx  x   xx xx  xx xx   xx   xx   xx
    .  xxxx    xx xx  xx xx   x x x x   xx
    .  xx  x   xx xx  xx xx   x  x  x  
    .  xxxx     xxx    xxx    x     x   xx
    """
    print(boomstring)
    #endGame()

def goBoomBigger():
    bombstring = """                       
                         \|/                          
                       `--+--'                        
                         /|\                          
                        ' | '                         
                          |                           
                          |                           
                      ,--'#`--.                       
                      |#######|                       
                   _.-'#######`-._                    
                ,-'###############`-.                 
              ,'#####################`,               
             /#########################\              
            |###########################|             
           |#############################|            
           |#############################|            
           |#############################|            
           |#############################|            
            |###########################|             
             \#########################/              
              `.#####################,'               
                `._###############_,'                 
                   `--..#####..--'
    """
    print(bombstring)

#level5.py
## move(sboard,mboard)
def move(sboard,mboard):
    if endOfGame(sboard,mboard)==0: return 2
    else: pass
        
    print("Which square do you wish to uncover?")
    loc=[int(x) for x in input("Enter a row and column, separated by a space:").split(" ")] 
    if showCell(sboard,mboard,loc): 
        goBoom() 
        return 1
    else: 
        displayBoard(sboard) 
        return 0

#game.py #maybe not needed
def playagain():
    choice = input('Play again? (y/n): ')
    return choice.lower() == 'y'
