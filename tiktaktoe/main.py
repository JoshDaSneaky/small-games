import os

#game grid, where 0 = empty, 1 = circle, -1 = cross

grid = {"top-left":" ", "top-middle":" ", "top-right":" ",
        "center-left":" ", "center-middle":" ", "center-right":" ",
        "bottom-left":" ", "bottom-middle":" ", "bottom-right":" "}

#function for drawing the grid
def draw(grid:dict):
    print(grid("top-left"), "|", grid("top-middle"), "|", grid("top-right"),sep="")
    print("-"*5)
    print(grid("center-left"), "|", grid("center-middle"), "|", grid("center-right"),sep="")
    print("-"*5)
    print(grid("bottom-right"), "|", grid("bottom-middle"), "|", grid("bottom-right"),sep="")


#flag to track current player
flag = 0

#initial command
command = input("start y/n")

if command == "y":
    gameOver = False
else:
    gameOver= True

#main loop
while not gameOver:
    if flag == 0:
        print("welcomt to tick Tack Toe")
        print("Player 1 Moves first")
        flag = 1
    elif flag == 1:
        pass

        # #I could honestly use a dictionary for all grid locations but its currently 3 am and im tired
        # if command == '1' and grid[0][0] != -1:
        #     grid[0][0] = 1
        # elif command == '2' and grid[0][1] != -1:
        #     grid[0][1] = 1


    os.system("clear")
    draw(grid)


    command = input(">>>")