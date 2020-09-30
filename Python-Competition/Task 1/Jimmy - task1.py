import random

game = 1
point = 0
while True:
    print("Let's row two dice. You will need to guess the sum of two dice. Good luck.")
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    while True:
        print('Now the dice had been raw. take a guess. (2~12)')
        guess = input()
        if guess.isdigit():
            guess = int(guess)
            if guess == x+y:
                point = point+1
                print('you had guess the right answer. Your point is', point, 'points.')
                break
            else:
                print('that is not the right answer. the right answer is', x+y,'. i will take off a mark from you.')
                point = point-1
                print('you have', point, 'points')
                break
            
        else:
            print('pleas input a number.')
            
    print('do you want to play again? please input yes or no otherwise the game will close.')
    playagain = input()
    if playagain == 'yes':
        game = game+1
    else:
        print('the game is closed, you have played', game, 'games. you have win', point, 'point. thank you for playing.')
        break
            
