
# Expected input range: None
# Output: Prints the title and rules of the game
def printTitle():
    str = '''
        ----------------     1 | 2 | 3
        TIC - TAC - TOE      4 | 5 | 6
        ----------------     7 | 8 | 9

        TO PLAY TIC - TAC - TOE, YOU NEED TO GET THREE IN A ROW.
        YOUR CHOICES ARE BETWEEN 1 TO 9.

        '''
    print(str)

# Expected input range: 1-9
# Output: Checks if a tile is avaliable
def isPositionAvaliable(tile):
    str = ''

# Expected input range: 1-9, choice of X or O
# Output: Prints the board with updated choices
def printBoard(tile, choice):
    str = '''
    1 | 2 | 3
    4 | 5 | 6
    7 | 8 | 9
    '''
    arr = [[1, 2, 3],
           [4, 5, 6],
           [7, 8 , 9]]
    for x in arr:
        if tile in x:
            arr[arr.index(x)][x.index(tile)] = choice

    for x in arr:
        for y in x:
            print(y, end = "|")
        print('\n')

# Expected input range: TBD
# Output: Checks if the game is over
def victoryCheck():
    str = ''
    
# Expected input range: TBD
# Output: Runs the other functions to play the game
def playGame():
    str = ''

def main():
    printTitle()


if(__name__ == "__main__"):
    main()
