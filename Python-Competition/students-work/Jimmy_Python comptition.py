print('Please input your number of range.')
x = input()


while True:
    if x.isdigit():
        print('The range is 1~', x)
        break
    else:
        print('The range should be number, please input again.')
        x = input()
    


