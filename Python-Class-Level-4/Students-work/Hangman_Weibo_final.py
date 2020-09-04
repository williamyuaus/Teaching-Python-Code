import random
HANGMAN_PICS = ['''
                  ____
                 |    |
                 |
                 |
                 |
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |
                 |
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |    |
                 |
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |   -|
                 |   
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |   -|-
                 |   
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |  \-|-
                 |   
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |  \-|-/
                 |   
                 |________''',  '''
                  ____
                 |    |
                 |    O
                 |  \-|-/
                 |     \ 
                 |________''', '''
                  ____
                 |    |
                 |    O
                 |  \-|-/
                 |   / \ 
                 |________'''] 
words = {'hostile': 'creeper slime zombie slime drowned witch vindicator evoker endermite hoglin zoglin guardian stray wither phantom pillager ravager skeleton vex husk shulker silverfish ghast'.split(),
        'neutral': 'bee piglin dolphin enderman spider llama panda wolf'.split(),
        'passive': 'pig cow sheep strider cod salmon mooshroom squid villager ocelot cat rabbit parrot turtle pufferfish bat horse donkey mule fox'.split()}
def getRandomWord(wordDict): 
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    
    return [wordDict[wordKey][wordIndex], wordKey] 
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print('Incorrect letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = (len(secretWord) * '_')

    for i in range(len(secretWord)):
          if secretWord[i] in correctLetters:
              blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
          print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print("What is your guess?")
        guess = input().lower()
        if len(guess) != 1: 
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a English letter.")
        else:
            return guess
            
def playAgain():
    print("Do you want to play again?")
    return input().lower().startswith('y')

print("H A N G M A N: MINECRAFT MOBS")
print("What difficulty do you want to play? E, M or H.")
difficulty = ' '
while difficulty not in 'EMH':
    print('Enter either E(easy), M(medium) or H(hard)')
    difficulty = input().upper()
    if difficulty == 'M':
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
    if difficulty == 'H':
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is a ' + secretSet + ' mob.')
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Well done! You survived!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Hangman is dead! The word was ' + secretWord + '.')
            gameIsDone = True

    if gameIsDone == True:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
        else:
            break
                
