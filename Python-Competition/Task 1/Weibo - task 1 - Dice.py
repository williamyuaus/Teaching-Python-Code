import random, sys

points = []
def getDiceOneNumber():
    diceOneNumber = random.randint(1, 6)
    return(diceOneNumber)
    
def getDiceTwoNumber():
    diceTwoNumber = random.randint(1, 6)
    return(diceTwoNumber)

result = (getDiceOneNumber() + getDiceTwoNumber())
print('In this game, the computer will roll to dice and add up their values. You have to guess the result.')
print('What is your guess?')
guess = input()
if guess != result:
    print('No, that is not the result.')
else:
    print('Well done!')
    points += 1
print('You have %s points.' %(points))
print('Do you want to try again?')
if input().lower().startswith('n'):
    print('Okay! Bye!')
    sys.exit()
else:
    getDiceOneNumber = True
    getDiceTwoNumber = True
