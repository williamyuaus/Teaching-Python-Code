def inputNumber():
    while True:
        print ('please enter a number between 0 and 5')
        number = input()
        
        if number.isdigit() == False:
            print ('please input a NUMBER')
            
        elif number in ['0', '1', '2', '3', '4', '5']:
            return number
        
        else:
            print ('The number you entered is not between 0 and 5')
    

print (inputNumber())
