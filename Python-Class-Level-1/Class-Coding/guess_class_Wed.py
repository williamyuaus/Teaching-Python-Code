import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

print('Well, ' + myName + ', I am thinking of a number between 1 and 20')
number = random.randint(1, 20)

for guessesTaken in range(6):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if guess < number:
        if guess > (number - 5):
            print('Your guess is a little lower')
        else:
            print('Your guess is too low.')

    if guess > number:
        if guess < (number + 5):
            print ('Your guess is a little higher')
        else:
            print('Your guess is too high.')

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') 

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
