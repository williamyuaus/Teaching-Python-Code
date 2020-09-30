import random
from time import sleep

def getDiceOneNumber():
    diceOneNumber = random.randint(1, 6)
    return diceOneNumber
def getDiceTwoNumber():
    diceTwoNumber = random.randint(1, 6)
    return diceTwoNumber



def drawBoard(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

        #the first element in the list is the player's letter, the second is the computer's letter
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

def whoGoesFirst():
    print('We\'ll ro')
    result = (getDiceOneNumber())
    sleep(1)
    print('The sum of the dice is %s.' %(result))
    if result == 2:
        print('+------+')
        print('|()    |')
        print('|      |')
        print('|    ()|')
        print('+------+')
        return 'player'
    elif result == 3:
        print('+------+')
        print('|()    |')
        print('|  ()  |')
        print('|    ()|')
        print('+------+')
        return 'computer'
    elif result == 4:
        print('+------+')
        print('|()  ()|')
        print('|      |')
        print('|()  ()|')
        print('+------+')
        return 'player'
    elif result == 5:
        
        print('+------+')
        print('|()  ()|')
        print('|  ()  |')
        print('|()  ()|')
        print('+------+')
        return 'computer'
    elif result == 6:
        print('+------+')
        print('|()()()|')
        print('|      |')
        print('|()()()|')
        print('+------+')
        return 'player'
    
    else:
        pass
        
def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or bo[3] == le and bo[5] == le and bo[7] ==le)

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def getPlayMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    if isSpaceFree(board, 5):
        return 5

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
    
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True
print("Welcome to Tic Tac Toe Extreme! Have fun, and try to beat our unstoppable computer!")

while True:
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first this time.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                print('Good job! You have done the impossible. You are now 1st in the world. But be careful- I shall have my revenge!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Bad Luck! Like we thought, you couldn't beat our super AI!") 
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    print('Do you want to try again? Y/N')
    if not input().lower().startswith('y'):
        break
    


