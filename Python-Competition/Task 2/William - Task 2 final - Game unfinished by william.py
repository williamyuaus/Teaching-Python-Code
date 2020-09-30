import random as ra
print('Hi, this is dies Cards, there is 3 small games in one big game. You win the big game if you win 2/3 small games,each time, you and the computer each get 9cards, you can either')
print('use them all or keep some for the next small game.')
print('there are 7 type of cards in total:')
print('S: get two random cards')
print('L:row two 6 side dices, add their point sum to your point')
print('TA:Two point Acards, each A cards in your grave will boost the next A card you play')
print('SA:Three point A card')
print('C:You can select a random card in your grave to go back to your deck')
print('R:Row a 6side dice, add the point to your point')
print('P: Row two 6side dice, minuce the sum of them from your points')
print('Please select the cards by typing their upper case names,if you want to end the small game, type 1 when asking. good day.')
S='S'
P='P'#SCORCH
L='L'#LEGEN
TA='TA'
SA='SA'
C='C'#CROW
R='R'#Random
cardPond=[R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,R,TA,TA,TA,TA,TA,TA,TA,TA,SA,SA,SA,SA,SA,SA,SA,P,P,S,S,L,L,L,L,L,L,P,P,P,P,S,S,S,C,C,C,C,C]
print(len(cardPond))
playerHand=[]
AIHand=[]
PlayerCardGrave=[]
AICardGrave=[]
j=3
gameIsPlaying=True
def playerCardValue(player_card,playerPoint):
    if player_card=='R':
        print('calc')
        playerPoint+=ra.randint(1,6)
        return playerPoint
    
           
    if player_card=='P':
        print('calc')
        sco=ra.randint(2,12)
        playeraPoint-=sco
        return playerPoint
    if player_card=='S':
        print('calc')
        for i in range(2):
            playerHand.append( ra.choice[R,TA,SA,P,S,L,C])
        
    if player_card=='L':
        print('calc')
        legend=ra.randint(2,12)
        print('legend value is'+str(legend))
        playerPoint+=legend
        return playerPoint
        
    if player_card=='C':
        print('calc')
        choice=input('which card you want to get back?')
        while choice not in PlayerCardGrave:
            print('select card in the grave')
            continue
        playerHand.append(choice)
    return playerPoint
def AICardValue(AiAttack,AiPoint):
    if AiAttack=='R':
        print('calc')
        AiPoint+=ra.randint(1,6)
        return AiPoint
    if AiAttack=='P':
        print('calc')
        sco=ra.randint(2,12)
        AiPoint-=sco
        return AiPoint
    if AiAttack=='S':
        print('calc')
        for i in range(2):
            AIHand.append(ra.choice[R,TA,SA,P,S,L,C])
    if AiAttack=='L':
        print('calc')
        legend=ra.randint(2,12)
        print('legend value is'+str(legend))
        AiPoint+=legend
        
    if AiAttack=='C':
        print('calc')
        choice=ra.choice(AICardGrave)
        AIHand.append(choice)
    return AiPoint
    
def smallGameIsPlaying(playerPoint,AiPoint,):
    if len (playerHand) and len(AIHand) ==0:
        if playerPoint>AiPoint:
            return 1
            print('u win')
        if AiPoint>playerPoint:
            return 2
            print('ai win')
        else:
            return 3
            print('draw')
        gameIsPlaying=False
        playerPoint=0
        AiPoint=0
    if int(input('want to end? 1=YES/0=NO?'))==1:
        if playerPoint>AiPoint:
            return 'a'
            print('u win')
        if AiPoint>playerPoint:
            
            print('ai win')
            return 'b'
        else:
            
            
            print('draw')
            return 'c'
        gameIsPlaying=False
        playerPoint=0
        AiPoint=0
    if int(input('want to end? 1=YES/0=NO?'))==1:
        gameIsPlaying=True
        
    else:
        gameIsPlaying=True
        
def whoGoesFirst():
    if ra.randint(0,1)==1:
        return 'player'
    else:
        return 'com'
def getPlayerFirstMove():
    while True:
        player_car=input('what card do you want to use?')
        if player_car not in playerHand:
            print('what do U mean, U don"have it')
            continue
        if player_car in playerHand:
            print('success')
            PlayerCardGrave.append(player_car)
            playerHand.remove(player_car)
        return player_car
def getAIMove():
    AiAttack=ra.choice(AIHand)
    print('success')
    AICardGrave.append(AiAttack)
    AIHand.remove(AiAttack)
    return AiAttack
def getInfo():
    print('AI point is'+str(AiPoint))
    print('your point is'+str(playerpoint))
    print('your card grave is '+str(PlayerCardGrave))
    print('your deck is'+str(playerHand))
    print('Ai card grave is'+str(AICardGrave))
    
    
    
    
    

while True:
    length=len (cardPond)
    playerpoint=0
    AiPoint=0
    PLAYERWIN=0
    COMWIN=0
    playerPoint=0
    if COMWIN==2:
        print('ai win')
        break
    if PLAYERWIN==2:
        print('player win')
        break
    dice=ra.randint(6,9)
    if dice==6:
        print('+----+')
        print('|*  *|')
        print('|*  *|')
        print('|*  *|')
        print('+----+')
    if dice==7:
        print('+----+')
        print('|* **|')
        print('|*  *|')
        print('|*  *|')
        print('+----+')
    if dice==8:
        print('+----+')
        print('|* **|')
        print('|* **|')
        print('|*  *|')
        print('+----+')
    if dice==9:
        print('+----+')
        print('|* **|')
        print('|* **|')
        print('|* **|')
        print('+----+')
              
    print('so the game starts, random cards generating...')
    for i in range(dice):
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
            playerpoint=playerCardValue(getPlayerFirstMove(),playerPoint)
            turn='com'
        if turn=='com':
            print('com go ')
            getAIMove()
            AICardValue(getAIMove(),AiPoint)
            turn='player'
        getInfo()
        smallGameIsPlaying(playerpoint,AiPoint)
        if smallGameIsPlaying(playerpoint,AiPoint)== 'a':
            print('u win')
        if smallGameIsPlaying(playerpoint,AiPoint)== 'b':
            print('ai win')
        if smallGameIsPlaying(playerpoint,AiPoint)=='c':
            print('draw')
    
    
        
