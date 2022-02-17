import random, sys, time

PAUSE_AMOUNT = 0.05  # (!) Try changing this to 0 or 1.0.
width = 20
leftWidth = 7
space = 5
change = 0
rightWidth = width - leftWidth - space
while True:
    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

    if leftWidth > 1 and width - leftWidth - space > 1:
        leftWidth += random.randint(-1, 1)
        rightWidth = width - leftWidth - space
        print('#' * leftWidth + ' ' * space + '#' * rightWidth)
    elif width - leftWidth - space <= 1:
        leftWidth += random.randint(-1, 0)
    elif leftWidth <= 1:
        leftWidth += random.randint(0, 1)
        
    change += random.randint(-1, 1)
    if change == -1 and space > 1:
        space += change
    elif change == 1 and leftWidth + space < width - 1:
        space += change
#r = random.randint(0, 3)
#while True:
#   if r == 0:
#       r = random.randint(0, 1)
#   print(width[r])
#   if r == 1:
#       r = random.randint(0, 2)
#   print(width[r])
#   if r == 2:
#       r = random.randint(1, 3)
#   print(width[r])
#   if r == 3:
#       r = random.randint(2, 3)
#       print(width[r])
    
