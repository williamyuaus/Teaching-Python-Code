print('Please input a number to be the range.')
number = int(input())
if number <= 0:
    print('Please enter a positive number greater than 0.')
elif number in '`@#$%^&*()_+-=!QWERTYUIOP{}|ASDFGHJKLZXCVBNM<>?qwertyuiopasdfghjkl;:"zxcvbnm,./' or number == "'":
    print('Please enter a number.')
else:
    print('Please input a number between 0 and your range.')
    number2 = int(input())
    if number2 > 0 and number2 < number:
        print('Yes, that is between 0 and your range.')
    else:
        print('No, thatnumber is not between 0 and your range.')
