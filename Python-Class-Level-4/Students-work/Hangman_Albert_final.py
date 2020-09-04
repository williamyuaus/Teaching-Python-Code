import random

HANGMAN_PICS = [
    '''       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
       |               \ |
                        \|
                         |
                         |
                         |
                         |
                         |
                         |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      /                \ |
     |                  \|
      -                  |
                         |
                         |
                         |
                         |
                         |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |   |              \|
      - -                |
                         |
                         |
                         |
                         |
                         |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      - -                |
                         |
                         |
                         |
                         |
                         |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      -|-                |
       |                 |
       |                 |
       |                 |
                         |
                         |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      -|-                |
       |                 |
       |                 |
       |                 |
      /                  |
     /                   |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      -|-                |
       |                 |
       |                 |
       |                 |
      / \                |
     /   \               |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      -|-                |
       |\                |
       | \               |
       |                 |
      / \                |
     /   \               |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''

       +-----------------+
       |  /        \     |
       | /          \    |
       |/            \   |
       |              \  |
      / \              \ |
     |( )|              \|
      -|-                |
      /|\                |
     / | \               |
       |                 |
      / \                |
     /   \               |
 +-----------------------+
 |                       |
 |                      /|\    
 |                     / | \\
 |____________________/__|__\____''','''
       +------------------+
       |  /         \     |
       | /           \    |
       |/             \   |
       |               \  |
       |                \ |
       |                 \|
       |                  |
       |                  |
      / \                 |
     |( )|                |
      -|-                 |
      /|\                 |
 +-- / | \   -------------+
 |     |                  |
 |    / \                /|\    
 |   /   \              / | \\
 |_____________________/__|__\____'''

                ]
words = {'animal' : 'ant baboon badger bat beaver camel cat clam cobra cougar coyote crow deer dog whale falcon eagle tiger lion lizard shark dolphin zebra penguin elephant termite wasp bull hawk swan clownfish octopus squid spider horse turtle dinosaur'.split(),
         'technology': 'computer laptop television console smartphone tablet smartwatch mouse keyboard monitor headphones touchscreen speaker bluetooth internet printer wireless microphone radio microwave laser system camera fingerprint robot'.split(),
         'food' : 'steak pasta meatball dumpling sushi ramen pie burger wrap cookie donut salad ratatoulie escargots croissant curry scone bacon prosciutto salami cheese sandwich bagel sausage tenders rice risotto risole bread barbecue marshmellow'.split(),
         'music' : 'piano forte pianoforte stave treble bass clef cadence chord crochet quaver minim breve semibreve clarinet saxophone harmony timbre rhythm tone pitch soprano alto tenor baritone jazz rock classical romantic baroque'.split(), 
         'hard' : 'pneumonoultramicroscopicsilicovolcanoconiosis pseudopseudohypoparathyroidism antidisestablishmentarianism floccinaucinihilipilification supercalifragilisticexpialidocious honorificabilitudinitatibus'.split()}
        

def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey])-1)

    return [wordDict[wordKey][wordIndex], wordKey] 
    
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print()
    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print (letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print ('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print ('Please enter a single letter')
        elif guess in alreadyGuessed:
            print ('You have already guesses this letter')
        elif guess not in ('abcdefghijklmnopqrstuvwxyz'):
            print ('Please enter a LETTER.')
        else:
            return guess
        
def playAgain():
    print ('Would you like to play another game, please type (y)es if you want to play again')
    return input().lower().startswith('y')


print ('H A N G M A N')
difficulty = ' '
while difficulty not in 'EMHNP':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard, N - Nightmare, P - Perfectionist')
    difficulty = input().upper()
    
if difficulty == 'M':
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]
    
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]
    
if difficulty == 'N':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]

if difficulty == 'P':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[6]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[4]
    del HANGMAN_PICS[3]
    del HANGMAN_PICS[2]
    del HANGMAN_PICS[1]
    

missedLetters = ''
correctLetters = ''
wordDict = words
secretWord, secretSet = getRandomWord(wordDict)
gameIsDone = False
print ('The secret word is from the "%s" set' %(secretSet))

while True:
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
            print('Yes! You found the secret word %s!' %(secretWord))
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print(('You have run out of guesses, you lose!\nAfter %s guesses you were not able to guess the secret word "%s"') % (len(HANGMAN_PICS) - 1, secretWord))
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters= ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(wordDict)
        else:
            break
    
