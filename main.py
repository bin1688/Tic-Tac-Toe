def printGameBoard(board):
    for i in board:
        print(end='          ')
        for j in i:
            print(j, end='')
        print()


def getLocation(userInput):
    if userInput == 1:
        return 0, 0
    elif userInput == 2:
        return 0, 2
    elif userInput == 3:
        return 0, 4
    elif userInput == 4:
        return 2, 0
    elif userInput == 5:
        return 2, 2
    elif userInput == 6:
        return 2, 4
    elif userInput == 7:
        return 4, 0
    elif userInput == 8:
        return 4, 2
    elif userInput == 9:
        return 4, 4


# def getSymbol()

def checkGame(board, location):

    if location in (1, 2, 3):
        if board[0][0] == whoTurn and board[0][2] == whoTurn and board[0][4] == whoTurn:
            return whoTurn
        elif location == 1:
            if board[2][0] == whoTurn and board[4][0] == whoTurn:
                return whoTurn
            elif board[2][2] == whoTurn and board[4][4] == whoTurn:
                return whoTurn
        elif location == 2:
            if board[2][2] == whoTurn and board[4][2] == whoTurn:
                return whoTurn
        else:
            if board[2][4] == whoTurn and board[4][4] == whoTurn:
                return whoTurn
            elif board[2][2] == whoTurn and board[4][0] == whoTurn:
                return whoTurn

    elif location in (4, 5, 6):
        if board[2][0] == whoTurn and board[2][2] == whoTurn and board[2][4] == whoTurn:
            return whoTurn
        elif location == 4:
            if board[2][2] == whoTurn and board[2][4] == whoTurn:
                return whoTurn

        elif location == 5:
            if board[0][2] == whoTurn and board[4][2] == whoTurn:
                return whoTurn
            elif board[0][4] == whoTurn and board[4][0] == whoTurn:
                return whoTurn
            elif board[0][0] == whoTurn and board[4][4] == whoTurn:
                return whoTurn
        else:
            if board[0][4] == whoTurn and board[4][4] == whoTurn:
                return whoTurn

    elif location in (7, 8, 9):
        if board[4][0] == whoTurn and board[4][2] == whoTurn and board[4][4] == whoTurn:
            return whoTurn
        elif location == 7:
            if board[0][0] == whoTurn and board[2][0] == whoTurn:
                return whoTurn
            elif board[2][2] == whoTurn and board[0][4] == whoTurn:
                return whoTurn
        elif location == 8:
            if board[2][2] == whoTurn and board[0][2] == whoTurn:
                return whoTurn
        else:
            if board[2][4] == whoTurn and board[0][4] == whoTurn:
                return whoTurn
            elif board[2][2] == whoTurn and board[0][0] == whoTurn:
                return whoTurn
    return ''


symbol = ''

gameBoard = [[' ', '|', ' ', '|', ' '],
             ['-', '+', '-', '+', '-'],
             [' ', '|', ' ', '|', ' '],
             ['-', '+', '-', '+', '-'],
             [' ', '|', ' ', '|', ' ']]

playAgain = 'y'

while playAgain == 'y':

    print("  Welcome to My Tic Tac Toe Game!\n")

    gameBoard = [[' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' ']]

    printGameBoard(gameBoard)
    print()

    count = 9
    whoTurn = 'X'
    while count != 0:

        if count % 2 != 0:
            symbol = 'X'
            whoTurn = 'X'
        else:
            symbol = 'O'
            whoTurn = 'O'

        position = int(input('   "' + whoTurn + '" enter your placement (1-9): '))
        print()
        x, y = getLocation(position)

        while gameBoard[x][y] == 'X' or gameBoard[x][y] == 'O':
            print('  Spot Already Placed! Reenter a new placement.')
            print()
            position = int(input('   "' + whoTurn + '" enter your placement (1-9): '))
            x, y = getLocation(position)

        gameBoard[x][y] = symbol
        printGameBoard(gameBoard)

        if count < 6:
            result = checkGame(gameBoard, position)
            if result != '':
                print('      ' + result + ' win!')
                break
        print()

        count -= 1

    if count == 0:
        print('      Tie\n')

    playAgain = input('  Do want play again (y/n)? ')
    print()
