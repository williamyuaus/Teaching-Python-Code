import random
import time

# Prints intro and instructions
def intro():
    print("Welcome to guess a number!")
    time.sleep(1)
    print("You will guess a number from 1 - 6 for each dice/die and we will roll a dice/die to see if your guess is correct! You will get a point if your guess is correct! Good luck!")
    time.sleep(2.5)

# Asks the user how many dice/die they want rol roll/guess
def how_many_dice():
    while True:
        try:
            num = int(input("Please enter how many dice/die you want to roll/guess (minimum is 1, maximum is 10): "))
        except ValueError:
            print("Invalid input, try again")
            continue
        if num >= 1 and num <= 10:
            return num
        else:
            print("Invalid input, try again")

# Gets the guesses of the numbers from the user and stores in a list
def guesses(num):
    guessesl = []
    for i in range(num):
        print("Dice", int(i + 1))
        time.sleep(0.5)
        while True:
            try:
                guess = int(input("Guess (between 1 & 6 inclusive): "))
            except ValueError:
                print("Invalid input, try again")
                continue
            if guess >= 1 and guess <= 6:
                guessesl.append(guess)
                break
            else:
                print("Invalid input, try again")
        time.sleep(0.5)
    return guessesl

# Rolls the dice and prints the result
def roll(num):
    time.sleep(1)
    print("Rolling dice/die...")
    time.sleep(2.5)
    nums = [1,2,3,4,5,6]
    rolll = []
    for i in range(num):
        rol = random.choice(nums)
        print("Dice", str(i + 1) + ":", rol)
        rolll.append(rol)
        time.sleep(1.5)
    return rolll

# Checks if user's guess is correct and adds up their points
def check(guessesl,rolll,num):
    time.sleep(1)
    print("Checking...")
    time.sleep(2.5)
    points = 0
    for i in range(num):
        if guessesl[i] == rolll[i]:
            print("Guess for dice", str(i + 1), "is: Correct!")
            points = points + 1
        else:
            print("Guess for dice", str(i + 1), "is: Incorrect!")
        time.sleep(1.5)
    return points

# The main function that runs everything
def main():
    intro()
    num = how_many_dice()
    time.sleep(0.5)
    print("You will guess", num, "number/numbers, and roll", num, "dice/die.")
    time.sleep(0.5)
    guessesl = guesses(num)
    rolll = roll(num)
    checkl = check(guessesl,rolll,num)
    time.sleep(1)
    print("Your final score is", checkl, "point/points!")
    time.sleep(1)
    print("Thank you for playing!")
    time.sleep(2)

# Runs the main functions and asks the user if they want to play again
while True:
    main()
    playagain = input("Play again? ('yes'/enter anything else to quit): ")
    if playagain == "yes":
        pass
    else:
        break