import random, sys
from time import sleep

DICE_FACES = ['''

''']

points = 0
def getDiceOneNumber():
    diceOneNumber = random.randint(1, 6)
    return(diceOneNumber)
    
def getDiceTwoNumber():
    diceTwoNumber = random.randint(1, 6)
    return(diceTwoNumber)

while True:
    result = (getDiceOneNumber() + getDiceTwoNumber())
    print('In this game, the computer will roll two dice and add up their values. You have to guess the result.')
    print('What is your guess?')
    while True:
        guess = int(input())
        if guess > 12:
            print("Invalid number - please try again")
        else:
            break
    print("Rolling...")
    sleep(2)
    
    if guess != result:
        print('No, that is not the result.')
        print('The result is ' + str(result))
    else:
        print('Well done!')
        points += 1
    print('You have %s points.' %(points))
    print('Do you want to try again?')
    if input().lower().startswith('n'):
        print('Okay! Bye!')
        sys.exit()

