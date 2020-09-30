import random
import sys

DICE_RANGE = []
WIDTH = 8
HEIGHT = 8
score = 0
diceGameChance = ['y']

def getNewBoard():
    board = []
    for i in range(WIDTH):
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def drawBoard(board):
    print('  12345678  ')
    print(' +--------+ ')
    for y in range(HEIGHT):
        print('%s|' %(y+1), end = '')
        for x in range (WIDTH):
            print(board[x][y], end ='')
        print('|%s' %(y+1))
    print(' +--------+ ')
    print('  12345678  ')


def isOnBoard(x, y):
    return x >= 0 and x <= WIDTH - 1 and y >= 0 and y <= HEIGHT - 1
    

def isValidMove(board, tile , xstart, ystart):
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection
        y += ydirection
        while isOnBoard(x, y) and board[x][y] == otherTile:
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def getBoardWithValidMoves(board, tile):
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = '.'
    return boardCopy

def getValidMoves(board, tile):
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile , x, y) != False:
                validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore += 1
            if board[x][y] == 'O':
                oscore += 1
    return {'X': xscore, 'O':oscore}

def enterPlayerTile():
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input().upper()

    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy

def getPlayerMove(board, playerTile):
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to toggle hints.')
        move = input().lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) == 2 and move [0] in DIGITS1TO8 and move [1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Enter the column (1-8) and then row (1-8).')
            print('For exmaple, 81 will move on the top-right corner.')
    return[x, y]

def isOnCorner(x, y):
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getComputerMove(board, computerTile):
    possibleMoves = getValidMoves(board, computerTile)
    random.shuffle(possibleMoves)

    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    bestScore = -1
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestScore = score
            bestMove = [x, y]
    return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile], scores[computerTile]))

#DICE GAME

def getDiceRange(DICE_RANGE):
    diceSides = random.randint(6, 6)
    for x in range (1, diceSides + 1):
        DICE_RANGE.append(x)
        x = x + 1
    return DICE_RANGE

def getPlayerGuess(DICE_RANGE):
    while True:
        guess = int(input())
        if guess in range (0, 2*DICE_RANGE[-1] + 1):
            return guess
        else:
            print('enter a VALID NUMBER please')


def diceRolls(DICE_RANGE):
    randomRolls = [random.choice(DICE_RANGE), random.choice(DICE_RANGE)]
    return randomRolls

def correctGuess():
    return diceRolls(DICE_RANGE)[0] + diceRolls(DICE_RANGE)[1]

def getGuesses():
    numGuesses = [2, 4, 6, 8]
    return random.choice(numGuesses)

#DICE GAME

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    
    board = getNewBoard()
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board

        elif turn == 'player':
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'quit':
                    print ('Thanks for playing!')
                    sys.exit()
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[0], move[1])

            if random.choice(diceGameChance) == 'y':
                    getDiceRange(DICE_RANGE)
                    guesses = getGuesses()
                    answer = correctGuess()
                    print ('You current score this session is %s' % (score))
                    print(DICE_RANGE)
                    print ('Let\' begin! Try to guess the sum of two random numbers between 1 and %s' % (DICE_RANGE[-1]))
                    print ()
                    for a in range (1, guesses + 1):
                        guess = getPlayerGuess(DICE_RANGE)
                        if guess == answer:
                           print ('You are correct')
                           print ()
                           print ('You guessed the number with %s guesses remaining, congratulations' % (guesses - 1))
                           print ()
                           turn = 'player'
                           continue
                        if guess < answer:
                           print ('Your guess is smaller than the answer')
                           print ()
                           print ('you have %s guess remaining' % (guesses -1))
                           print ()
                        if guess > answer:
                           print ('Your guess is larger than the answer')
                           print ()
                           print ('you have %s guess remaining' % (guesses -1))
                           print ()
                        guesses = guesses - 1
                        if guesses == 0:
                           turn = 'computer'
                           continue
                
            else:
                turn = 'computer'

        elif turn == 'computer':
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Press Enter to see the computer\'s move.')

                move = getComputerMove(board, computerTile)
                makeMove (board, computerTile, move[0], move[1])

            turn = 'player'

print('Welcome to Reverse Game!')

playerTile, computerTile = enterPlayerTile()


while True:
    finalBoard = playGame(playerTile, computerTile)

    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s point. O scored %s points.' %(scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print ('You lost. The computre beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        print('This game is a tie')

    print('Do you want to play again? (yes or no)')
    if not input().lower().startswith('y'):
        break




while True:
    getDiceRange(DICE_RANGE)
    guesses = getGuesses()
    answer = correctGuess()
    print ('You current score this session is %s' % (score))
    print ('Let\' begin! Try to guess the sum of two random numbers between 1 and %s' % (DICE_RANGE[-1]))
    print ()
    for a in range (1, guesses):
         guess = getPlayerGuess(DICE_RANGE)
         if guess == answer:
            print ('You are correct')
            print ()
            print ('You guessed the number with %s gueses remaining, congratulations' % (guesses - a))
            print ()
            score = score + 1
            break
         if guess < answer:
            print ('Your guess is smaller than the answer')
            print ()
            print ('you have %s guess remaining' % (guesses - a))
            print ()
         if guess > answer:
            print ('Your guess is larger than the answer')
            print ()
            print ('you have %s guess remaining' % (guesses - a))
            print ()
            


                        
            


