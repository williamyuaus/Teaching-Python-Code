"""
Number Guess
Wanna play a game? In this project, we'll build a program that rolls a pair of dice and asks the user to guess the sum. If the user's guess is equal to the total value of the dice roll, the user wins! Otherwise, the computer wins.

The program should do the following:

Roll a pair of dice.
Add the values of the roll.
Ask the user to guess a number.
Compare the user's guess to the total value.
Determine the winner (user or computer).
Let's begin!

"""
from random import randint


from time import sleep


def get_user_guess():
  guess = int(input("Guess a number!"))
  return guess

def roll_dice(sides):
  first_roll = randint(1,sides)
  second_roll = randint(1,sides)
  max_val = sides*2
  print("The maximum value is {}".format(max_val))
  guess = get_user_guess()
  if guess > max_val:
    print("Invalid number - please try again")
  else:
      print("Rolling...")
      sleep(2)
      print("The 1st roll is: {}".format(first_roll))
      print("The 2nd roll is: {}".format(second_roll))
      total_roll = first_roll + second_roll
      print("Result...")
      sleep(1)
      if guess == total_roll:
        print("YOU WON! :)))")
      else:
        print('You Lost!')


roll_dice(6)


