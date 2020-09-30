import random as R
import sys as s

while True:
    print('game starts again!')
    die1=R.randint(1,6)
    die2=R.randint(1,6)
    summ=die1+die2
    count=5
    while True:
        guess= input('what is your guess?')
        if guess not in '0 1 2 3 4 5 6 7 8 9 10 11 12'.split():
            print('stop being a fool')
            continue
        guess=int(guess)
        if count==0:
            print('loser,answer is '+str(summ)+'again?yes?')
            if input()=='yes':
                break
            else:
                print('bye')
                s.exit()
        if guess == summ:
            print('you win, again?, yes?')
            if input()=='yes':
                break
            else:
                print('bye')
                s.exit()
        if guess != summ:
            print(str(guess),str(summ))
            print('wrong,U"ve got'+str(count)+'more chances')
            int (guess)
            int(summ)
            count-=1
            if summ>guess:
                print('toooo small')
            else:
                print('toooo big')
            continue
        
