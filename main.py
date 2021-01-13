board = [
    ['_','_','_'],
    ['_','_','_'],
    ['_','_','_']
]

ai = True

def print_board(board):
    for row in board:
        for pos in row:
            print(pos, end=' ')
        print('\n')

player = 'o'
computer = 'x'

def isMovesLeft(board) :

    for i in range(3) :
        for j in range(3) :
            if (board[i][j] == '_') :
                return True
    return False

def evaluate(b) :

    for row in range(3) :
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :
            if (b[row][0] == computer) :
                print('Computer wins')
                return 10
            elif (b[row][0] == player) :
                print('You win')
                return -10

    for col in range(3) :

        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :

            if (b[0][col] == computer) :
                print('Computer wins')
                return 10
            elif (b[0][col] == player) :
                print('You win')
                return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :

        if (b[0][0] == computer) :
            print('Computer wins')
            return 10
        elif (b[0][0] == player) :
            print('You win')
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :

        if (b[0][2] == computer) :
            print('Computer wins')
            return 10
        elif (b[0][2] == player) :
            print('You win')
            return -10

    return -1

def minimax(board, depth, isMax) :

    if (isMax) :
        best = -1000

        for i in range(3) :
            for j in range(3) :

                if (board[i][j]=='_') :

                    board[i][j] = computer

                    best = max( best, minimax(board,
                                            depth + 1,
                                            not isMax) )

                    board[i][j] = '_'
        return best

    else :
        best = 1000

        for i in range(3) :
            for j in range(3) :

                if (board[i][j] == '_') :

                    board[i][j] = player
                    best = min(best, minimax(board, depth + 1, not isMax))

                    board[i][j] = '_'
        return best

def findBestMove(board) :
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3) :
        for j in range(3) :

            if (board[i][j] == '_') :

                board[i][j] = computer

                moveVal = minimax(board, 0, False)

                board[i][j] = '_'

                if (moveVal > bestVal) :
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

def check_input(user_input):
    if not user_input.isnumeric():
        return False

    user_input = int(user_input)
    if user_input > 9 or user_input < 1:
        return False

    return True

def quit(user_input):
    if user_input == 'q':
        return True
    else:
        return False

def coordinates(user_input):
    row = int(user_input/3)
    col = user_input
    if(col > 2):
        col = int(col%3)
    return (row,col)

def isTaken(coords, board):
    row = coords[0]
    col = coords[1]

    if board[row][col] != '_':
        print("It's already taken!")
        return True
    else:
        return False

def addToBoard(user_input, board, user):
    board[user_input[0]][user_input[1]] = user

while True:
    print_board(board)
    if not isMovesLeft(board):
        print('It\'s a tie')
        break
    if(ai):
        user = 'x'
        bestMove = findBestMove(board)
        addToBoard(bestMove, board, user)
    else:
        user = 'o'
        user_input = input('Enter a position from 1 to 9 or '
                           'enter \"q\" to quit:')
        if quit(user_input):
            break

        if not check_input(user_input):
            print('Please try again')
        else:
            user_input = int(user_input) - 1
            coords = coordinates(user_input)

            if isTaken(coords, board):
                print('Please try again')
            else:
                addToBoard(coords, board, user)
    if evaluate(board) == 10 or evaluate(board) == -10:
        print_board(board)
        break
    ai = not ai


