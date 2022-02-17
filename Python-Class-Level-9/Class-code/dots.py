from timeit import repeat


dots = list(range(1, 34))
increments = dots
# increments = list(range(1, 89))
for increment in increments:
    
    testDots = 1
    drawing = []
    repeat = 0
    while (repeat < 100):
        if (testDots in dots and testDots not in drawing):
            drawing.append(testDots)
            drawing.sort()
            if (len(drawing) == len(dots)):
                print(increment)
                # print (drawing)
        testDots += increment
        if (testDots > len(dots)):
            testDots -= len(dots)
            repeat += 1

    
