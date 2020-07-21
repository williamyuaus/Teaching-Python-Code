import random, sys

print('ROCK, PAPER, SCISSORS')

# variables for wins, losses and ties
wins = 0
losses = 0
ties = 0


# valiadate input
while True:
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit()
        if playerMove =='r' or playerMove == 'p' or playerMove =='s':
            break
        print("Type one of r, p, s, or q.")


    # Display the player move
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')


    # Display the computer move
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'p'
        print('PAPER')
    
    


    # Display and record win/loss/tie:






    
