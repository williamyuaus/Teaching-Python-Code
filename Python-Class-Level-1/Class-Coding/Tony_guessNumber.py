import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 50)
print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')

for guessesTaken in range(8):
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    if (guess < number):
        if guess > (number - 5):
            print('A little lower')
        else:
            print('Too low')

    if (guess > number):
        if guess < (number + 5):
            print('A little higher')
        else:
            print('Too high')

    if (guess == number):
        break

if (guess == number):
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if (guess != number):
    number = str(number)
    print('Nope. The number was ' + number + '.')

    
