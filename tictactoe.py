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

# For coloring the text
class colors:
    reset='\033[0m'
    class fg:
        black='\033[30m'
        enemy='\033[31m' # Red
        player='\033[32m' # Green
    class bg:
        green='\033[42m'
        red='\033[41m'

# Tracks the scores of the player and enemy
playerScore = 0
enemyScore = 0

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

# Expected input range: 1 to 9
# Output: Converts to int
def checkInt(choice):
    try:
        choice = int(choice)
    except(ValueError):
        choice = int(input(colors.fg.enemy + "Please choose a valid tile: " + colors.reset))
        if(choice > 9) or (choice < 1):
            choice = int(input(colors.fg.enemy + "Please choose a valid tile: " + colors.reset))
    return(choice)

# Expected input range: 1-9
# Output: Checks if a tile is avaliable, returns bool
def isPositionAvaliable(tile, board):
    for row in board:
        for col in row:
            if (type(tile) == str):
                return(False)
    return(True)

# Expected input range: Array and a character
# Output: Prints victory board for player
def printBoardPlayer(board, choice):
    count = 0
    for row in board:
        for col in row:
            if(col == choice):
                if(count % 2 == 0) and (count != 0):
                    print(colors.bg.green + colors.fg.black + 'O' + colors.reset, end = "")
                else:
                    print(colors.bg.green + colors.fg.black +  'O' + colors.reset, end = " | ")
            elif(col != choice) and (type(col) == str):
                if(count % 2 == 0) and (count != 0):
                    print(colors.fg.enemy + 'X' + colors.reset, end = "")
                else:
                    print(colors.fg.enemy + 'X' + colors.reset, end = " | ")
            elif(col % 3 == 0):    
                print(col, end = "")
            else:
                print(col, end = " | ")

            count += 1
        print("\t")
        count = 0
    global playerScore
    playerScore += 1

# Expected input range: Array and a character
# Output: Prints victory board for enemy
def printBoardEnemy(board, choice):
    count = 0
    for row in board:
        for col in row:
            if(col == choice):
                if(count % 2 == 0) and (count != 0):
                    print(colors.bg.red + colors.fg.black + 'X' + colors.reset, end = "")
                else:
                    print(colors.bg.red + colors.fg.black +  'X' + colors.reset, end = " | ")
            elif(col != choice) and (type(col) == str):
                if(count % 2 == 0) and (count != 0):
                    print(colors.fg.player + 'O' + colors.reset, end = "")
                else:
                    print(colors.fg.player + 'O' + colors.reset, end = " | ")
            elif(col % 3 == 0):    
                print(col, end = "")
            else:
                print(col, end = " | ")

            count += 1
        print("\t")
        count = 0
    global enemyScore
    enemyScore += 1

# Expected input range: string, array
# Output: Prints the board with updated choices
def printBoard(board, player):
    # Prints the board
    count = 0

    if(victoryCheck(board)):
        if(player == 1):
            printBoardPlayer(board, 'O')
        elif(player == 2):
            printBoardEnemy(board, 'X')
    if (victoryCheck(board) == False):
        for row in board:
            for col in row:
                if(type(col) == str):
                        if(col == 'O'):
                            if(count % 2 == 0) and (count != 0):
                                print(colors.fg.player + 'O' + colors.reset, end = "")
                            else:
                                print(colors.fg.player + 'O' + colors.reset, end = " | ")
                        elif(col == 'X'):
                            if(count % 2 == 0) and (count != 0):
                                print(colors.fg.enemy + 'X' + colors.reset, end = "")
                            else:
                                print(colors.fg.enemy + 'X' + colors.reset, end = " | ")
                elif(col % 3 == 0):    
                    print(col, end = "")
                else:
                    print(col, end = " | ")

                count += 1
            print("\t")
            count = 0

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

# Expected input range: Array and choice for player/enemy
# Output: Checks if the game is over, returns bool
def victoryCheck(board):
    count = 0
    for row in board:
        if all(letter == 'X' for letter in row):
            return(True)
        elif all(letter == 'O' for letter in row):
            return(True)
        for col in range(len(row)):
            if(type(row[col]) == str):
                if(col + 1 < 3) and (count + 1 < 3):
                    if(board[count][0] == board[count+1][1] == board[count+2][2]):
                        return(True)
                    elif(board[count][col] == board[count-1][col+1] == board[count+1][col-1]):
                        return(True)
                    elif(board[count][col] == board[count+1][col] == board[count+2][col]):
                        return(True)
        count += 1

    return(False)
    
# Expected input range: Array
# Output: Runs the other functions to play the game
def playGame(board, playerChoice, enemyChoice):
    tilePlayer = input(colors.fg.player + "Player 1" + colors.reset + ", Please choose a tile: ")
    tilePlayer = checkInt(tilePlayer)
    while(isPositionAvaliable(tilePlayer, board) == False):
        tilePlayer = int(input(colors.fg.enemy + "Please choose a different tile: " + colors.reset))  
    else:
        board = updateBoard(tilePlayer, playerChoice, board)
        printBoard(board, 1)
        if(victoryCheck(board)):
            return(board)

    tileEnemy = input(colors.fg.enemy + "Player 2" + colors.reset + ", Please choose a tile: ")
    tileEnemy = checkInt(tileEnemy)
    while(isPositionAvaliable(tileEnemy, board) == False):
        tileEnemy = int(input(colors.fg.enemy + "Please choose a different tile: " + colors.reset))  
    else:
        board = updateBoard(tileEnemy, enemyChoice, board)
        printBoard(board, 2)
        if(victoryCheck(board)):
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

    player = 'O'
    enemy = 'X'

    while (result != True):
        playGame(board, player, enemy)
        result = victoryCheck(board)

    if(result == True):
        print("You win! Thanks for playing!")
        print("The score is:\n Player 1: " + colors.fg.player + "% s" % playerScore + colors.reset + "\n Player 2: " + colors.fg.enemy + "% s" % enemyScore + colors.reset)
    else:
        print("You lose! Good luck next time.")
        print("The score is:\n Player 1: " + colors.fg.player + "% s" % playerScore + colors.reset + "\n Player 2: " + colors.fg.enemy + "% s" % enemyScore + colors.reset)

"""
For AI, use secrets from rand for more random choices, lowest level AI is just choosing randomly,
without regard for player choice, can make AI smarter by having checks to see where player places
their choices, and tries to block their moves
Docs: https://docs.python.org/3/library/random.html
"""

if(__name__ == "__main__"):
    main()
    loop()