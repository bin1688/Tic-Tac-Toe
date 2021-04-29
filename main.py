def printGameBoard(board):
    for i in board:
        print(end='              ')
        for j in i:
            print(j, end='')
        print()


def getLocation(userInput):
    userInput -= 1
    locationList = [(0, 0),
                    (0, 2),
                    (0, 4),
                    (2, 0),
                    (2, 2),
                    (2, 4),
                    (4, 0),
                    (4, 2),
                    (4, 4)]
    return locationList[userInput]


def checkGame(board, location, whoTurn):
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

    print("   Welcome to My Tic Tac Toe Game!\n")

    gameBoard = [[' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' '],
                 ['-', '+', '-', '+', '-'],
                 [' ', '|', ' ', '|', ' ']]

    printGameBoard(gameBoard)
    print()

    count = 9
    turn = 'X'
    while count != 0:

        if count % 2 != 0:
            symbol = 'X'
            turn = 'X'
        else:
            symbol = 'O'
            turn = 'O'

        position = int(input('   "' + turn + '" enter your placement (1-9): '))
        print()
        x, y = getLocation(position)

        while gameBoard[x][y] == 'X' or gameBoard[x][y] == 'O':
            print('  Spot Already Placed! Reenter a new placement.')
            print()
            position = int(input('   "' + turn + '" enter your placement (1-9): '))
            x, y = getLocation(position)

        gameBoard[x][y] = symbol
        printGameBoard(gameBoard)

        if count < 6:
            result = checkGame(gameBoard, position, turn)
            if result != '':
                print('\n   --------- "' + result + '" WIN! -----------')
                break

        count -= 1

    print()

    if count == 0:
        print('      Tie\n')

    playAgain = input('  Do you want to play again (y/n)? ')
    print()
