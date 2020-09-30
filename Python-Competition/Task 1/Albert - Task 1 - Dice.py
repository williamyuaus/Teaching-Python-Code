import random

DICE_RANGE = []

print ('This is a guess the sum of two numbers game')
print ()

def getDiceRange(DICE_RANGE):
    print ('Now let\'s set the die range from 1 to any number of your choice')
    print ('input your range below')
    diceSides = int(input())
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

def playAgain():
    print ('Would you like to play again? Type \'y\' if yes.')
    choice = input().lower()
    return choice

print('Firstly, how many guesses would you like to have, less = more difficult')
print ()
guesses = int(input())
getDiceRange(DICE_RANGE)
score = 0

while True:
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
            

    if playAgain() == 'y':
        continue
    else:
        print ('Play again soon!')
        break
    


