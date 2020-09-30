import random as ra
S='S'
P='P'#SCORCH
L='L'#LEGEN
TA='2A'
SA='3A'
C='C'#CROW
R='R'#Random
cardPond=[R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,TA,TA,TA,TA,TA,TA,TA,TA,SA,SA,SA,SA,SA,SA,SA,P,P,S,S,L,L,L,L,L,L,P,P,P,P,S,S,S,C,C,C,C,C]
print(len(cardPond))
playerHand=[]
AIHand=[]
PlayerCardGrave=[]
AICardGrave=[]
playerPoint=0
AiPoint=0
j=3
gameIsPlaying=True
def playerCardValue():
    if player_card='R':
        playerPoint+=ra.randint(1,6)
    if player_card='TA':
        if 
        playerPoint+=
    if player_card='SA':
    if player_card='P':
    if player_card='S':
    if player_card='L':
    if player_card='C':
    
def smallGameIsPlaying():
    if len (playerHand) and len(AIHand) ==0:
        gameIsPlaying=False
    if input('want to end? YES/NO?')=='Yes'or'YES'or'yes':
        gameIsPlaying=False
    else:
        gameIsPlaying=True
        
def whoGoesFirst():
    if ra.randint(0,1)==1:
        return 'player'
    else:
        return 'com'
def getPlayerFirstMove():
    while True:
        player_card=input('what card do you want to use?')
        if player_card not in playerHand:
            print('what do U mean, U don"have it')
            continue
        if player_card in playerHand:
            print('success')
            PlayerCardGrave.append(player_card)
            playerHand.remove(player_card)
        break
def getAIMove():
    AiAttack=ra.choice(AIHand)
    print('success')
    AICardGrave.append(AiAttack)
    AIHand.remove(AiAttack)
def getInfo():
    print('your card grave is '+str(PlayerCardGrave))
    print('your deck is'+str(playerHand))
    print('Ai card grave is'+str(AICardGrave))
    print('AI point is'+str(AiPoint))
    print('your point is'+str(playerPoint))
    
    
    
    
for x in range(0,j):
    length=len (cardPond)
    while gameIsPlaying==True:
        print('so the game starts, random cards generating...')
        for i in range(int(length/6)):
            randomCard= ra.choice(cardPond)
            playerHand.append(randomCard)
            cardPond.remove(randomCard)
            randomCardA=ra.choice(cardPond)
            AIHand.append(randomCardA)
            cardPond.remove(randomCardA)
        print('your hand is'+str(playerHand))
        whoGoesFirst()
        turn=whoGoesFirst()
        while gameIsPlaying:
            if turn=='player':
                print('U go ')
                getPlayerFirstMove()
                turn='com'
            if turn=='com':
                print('com go ')
                getAIMove()
                turn='player'
            smallGameIsPlaying()
            getInfo()
    
        
