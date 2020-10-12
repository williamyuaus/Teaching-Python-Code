import random
import sys
import math

def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    return board

def drawBoard(board):
    tensDigitsLine = '    '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    print()

    for row in range(15):
        # Single-digit numbers need to be padded with an extra space.
        if row < 10:
            extraSpace = ' '
        else:
            extraSpace = ''



        print('%s%s %s' % (extraSpace, row, row))


def showInstructions():
    print('''Instructions:
You are the captain of the Simon, a treasure-hunting ship. Your current mission
is to use sonar devices to find three sunken treasure chests at the bottom of
the ocean. But you only have cheap sonar that finds distance, not direction.

Enter the coordinates to drop a sonar device. The ocean map will be marked with
how far away the nearest chest is, or an X if it is beyond the sonar device's
range. For example, the C marks are where chests are. The sonar device shows a
3 because the closest chest is 3 spaces away.

1 2 3
012345678901234567890123456789012

0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
3 ````````~~~`````~~~`~`````~`~``~` 3
4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

012345678901234567890123456789012
1 2 3
(In the real game, the chests are not visible in the ocean.)

Press enter to continue...''')
    input()

    print('''When you drop a sonar device directly on a chest, you retrieve it and the other
sonar devices update to show how far away the next nearest chest is. The chests
are beyond the range of the sonar device on the left, so it shows an X.

1 2 3
012345678901234567890123456789012

0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
3 ````````~~~`````~~~`~`````~`~``~` 3
4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

012345678901234567890123456789012
1 2 3

The treasure chests don't move around. Sonar devices can detect treasure chests
up to a distance of 9 spaces. Try to collect all 3 chests before running out of
sonar devices. Good luck!

Press enter to continue...''')
    input()

theBoard = getNewBoard()
drawBoard(theBoard)









