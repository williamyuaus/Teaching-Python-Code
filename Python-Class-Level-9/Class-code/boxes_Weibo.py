import random
boxes = ['''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/''', '''
            ________
           /       /|
          /_______/ |
         |    o   | |
         |    |   | |
         |________| |
         |________|/'''
         
]
bombBox = '''
               ________
              /       /|
             /_______/ |
            |    o   | |
            |____|___|/|
             /   ,   | |
            /___()__/ /
           |________|/'''
             
carrotBox = '''
               ________
              /       /|
             /_______/ |
            |    o   | |
            |____|___|/|
             /  ()   / |
            /___\/__/ /
           |________|/'''
score1 = 0
score2 = 0
print('What is your name, P1?')
name1 = input()
print('What is your name. P2?')
name2 = input()
def askP1(score2):
    print('What box do you want to put the carrot in, ' + name1 + '?')
    correctBox = input()
    while correctBox not in '1 2 3 4 5 6 7 8'.split():
        print('Please enter a number between 1 and 8.')
        correctBox = input()
    correctBox = int(correctBox)
    boxes[correctBox - 1] = carrotBox
    bombBoxNum = random.randint(1, 8)
    while bombBoxNum == correctBox:
        bombBoxNum = random.randint(1, 8)
    #print(bombBoxNum)
    for box in boxes:
        print(box)
    input('Press enter to clear the screen.')
    for i in range(70):
        print('')
    #print('\n' * 70)
    print('Open your eyes, ' + name2 + '.')
    guess = input('What box do you want to open?')
    if int(guess) == correctBox:
        print('That was correct!')
        score2 += 1
    else:
        correctBox = str(correctBox)
        print('The carrot was in box ' + correctBox + '.')
        if int(guess) == bombBoxNum:
            score2 -= 1
            print('Oops... better visit a hospital.')
    viewB = input('Press enter to view boxes.')
    if viewB == '':
        for box in boxes:
            print(box)
    print('The score for ' + name2 + ' is ' + str(score2))
    askP2(score1)

def askP2(score1):
    print('What box do you want to put the carrot in, ' + name2 + '?')
    correctBox = input()
    while correctBox not in '1 2 3 4 5 6 7 8'.split():
        print('Please enter a number between 1 and 8.')
        correctBox = input()
    correctBox = int(correctBox)
    boxes[correctBox - 1] = carrotBox
    bombBoxNum = random.randint(1, 8)
    while bombBoxNum == correctBox:
        bombBoxNum = random.randint(1, 8)
    for box in boxes:
        print(box)
    input('Press enter to clear the screen.')
    for i in range(70):
        print('')
    #print('\n' * 70)
    print('Open your eyes, ' + name1 + '.')
    guess = input('What box do you want to open?')
    if int(guess) == correctBox:
        print('That was correct!')
        score1 += 1
    else:
        correctBox = str(correctBox)
        print('The carrot was in box ' + correctBox + '.')
        if int(guess) == bombBoxNum:
            score1 -= 1
            print('Oops... better visit a hospital.')
    viewB = input('Press enter to view boxes.')
    if viewB == '':
        for box in boxes:
            print(box)
    print('The score for ' + name1 + ' is ' + str(score1))
    askP1(score2)

askP1(score2)
