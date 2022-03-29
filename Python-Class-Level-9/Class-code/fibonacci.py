import sys
while True:
    print('This program can tell you what the x digit of the Fibonacci sequence is.')
    while True:
        print('Enter the digit you want to know.')
        wanted_number = input('> ').upper()
        if wanted_number == 'QUIT':
            sys.exit()
        if wanted_number.isdecimal() and int(wanted_number) != 0:
            wanted_num = int(wanted_number)
            break
        print('Please enter a whole number larger then 0.')
    if wanted_num == 1:
        print('0')
        continue
    elif wanted_num == 2:
        print('1')
    elif wanted_num == 3:
        print('1')
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    while True:
        nextNumber = secondToLastNumber + lastNumber
        print(nextNumber, end='')
        fibNumbersCalculated += 1
        if fibNumbersCalculated == wanted_num:
            print(nextNumber)
            break
        print(', ', end='')
        secondToLastNumber = lastNumber
        lastNumber = nextNumber