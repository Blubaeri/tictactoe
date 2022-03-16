"""
class colors:
    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'
    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
"""

class colors:
    reset='\033[0m'
    class fg:
        black='\033[30m'
        enemy='\033[31m' # Red
        player='\033[32m' # Green
    class bg:
        green='\033[42m'

class player():
    score = 0

# Expected input range: None
# Output: Checks if user wants to play again
def loop():
    user = input("Would you like to play again? (yes or no): ")
    if(user.lower() == 'yes'):
        main()
        loop()
    else:
        print("Goodbye!")
        return(False)

# Expected input range: 1-9
# Output: Checks if a tile is avaliable, returns bool
def isPositionAvaliable(tile, board):
    for row in board:
        for col in row:
            if (type(tile) == str):
                return(False)
    return(True)

# Expected input range: 1-9, string, array
# Output: Prints the board with updated choices
def printBoard(tile, choice, board):
    # Prints the board
    count = 0
    if (victoryCheck(board) == False):
        for row in board:
            for col in row:
                if(col == choice):
                    if(count % 2 == 0) and (count != 0):
                        print(colors.fg.player + col + colors.reset, end = "")
                    else:
                        print(colors.fg.player + col + colors.reset, end = " | ")
                elif(col % 3 == 0):    
                    print(col, end = "")
                else:
                    print(col, end = " | ")

                count += 1
            print("\t")
            count = 0
    else:
        for row in board:
            for col in row:
                if(col == choice):
                    if(count % 2 == 0) and (count != 0):
                        print(colors.bg.green + colors.fg.black + col  + colors.reset, end = "")
                    else:
                        print(colors.bg.green + colors.fg.black +  col + colors.reset, end = " | ")
                elif(col % 3 == 0):    
                    print(col, end = "")
                else:
                    print(col, end = " | ")

                count += 1
            print("\t")
            count = 0
    print("------------------")

# Expected input range: 1-9, string, array
# Output: Returns a updated board
def updateBoard(tile, choice, board):
    # Loops through the array and checks which tile to replace with 
    # the choice       
    for row in board:
        if tile in row:
            board[board.index(row)][row.index(tile)] = choice
            break
    return(board)

# Expected input range: Array
# Output: Checks if the game is over, returns bool
def victoryCheck(board):
    d1 = [1,5,9] 
    for row in board:
        if all(choice == 'X' for choice in row):
            return(True)
        elif all(choice == 'O' for choice in row):
            return(True)
    

    return(False)
    
# Expected input range: Array
# Output: Runs the other functions to play the game
def playGame(board, choice):
    tile = int(input("Please choose a tile: "))
    while(isPositionAvaliable(tile, board) == False):
        tile = int(input("Please choose a different tile: "))  
    else:
        board = updateBoard(tile, choice, board)
        printBoard(tile, choice, board)

    return(board)


def main():
    str = '''
        ----------------     1 | 2 | 3
        TIC - TAC - TOE      4 | 5 | 6
        ----------------     7 | 8 | 9

        TO PLAY TIC - TAC - TOE, YOU NEED TO GET THREE IN A ROW.
        YOUR CHOICES ARE BETWEEN 1 AND 9.

        '''
    print(str)
    result = False
    board = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
    choice = input("Please choose X or O: ")
    choice = choice.upper()
    while (result != True):
        playGame(board, choice)
        result = victoryCheck(board)
    if(result == True):
        print("You win! Thanks for playing!")
    else:
        print("You lose! Good luck next time.")

if(__name__ == "__main__"):
    main()
    loop()