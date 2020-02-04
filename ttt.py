###################################################################
## This is the main routine
## Empty spaces are _, User is o, System is x
###################################################################
if __name__ == "__main__":      ##you can google this to find out what it does
    grid = [["_" for x in range(3)] for y in range(3)]  ##initialize grid to empty, which is "_"
    draw_grid(grid)
    gameInProgress = 1          ## initialize to yes
    gameState = 3               ## States are: 0-System lost 1-User lost 2-Draw 3-Game in progress
    while gameInProgress:
        userMove = input("Your move: ")
        ## Try to make the user's move and check if valid. If not a valid move, ask again.
        while not make_move(grid, userMove, "o") == 1:
            userMove = input("Not an empty space. Try again: ")
        sys_move(grid)           ## Make the system's move
        draw_grid(grid)
        gameState = game_state(grid)     ## Check if game is over
        if gameState != 3: gameInProgress = 0
        ## End of While loop
        
    if gameState == 0: print("You won!")
    elif gameState == 1: print("I won!")
    elif gameState == 2: print("Draw.")

