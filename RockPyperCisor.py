from random import randint

def init():
    print('1: cisor')
    print('2: paper')
    print('3: rock')    

def fight(p1, p2):
    print(p1 , p2)

    if(p1 == p2):
        result = 'equality'
    elif(p1 == 1) and (p2 == 2):
        result = 'cisor vs paper : win'
    elif(p1 == 1) and (p2 == 3):
        result = 'cisor vs rock : loose'
    elif(p1 == 2) and (p2 == 1):
        result = 'paper vs rock : win'
    elif(p1 == 2) and (p2 == 3):
        result = 'paper vs cisor : loose'
    elif(p1 == 3) and (p2 == 1):
        result = 'rock vs cisor : win'
    elif(p1 == 3) and (p2 == 2):
        result = 'rock vs paper : loose'
    print(result)

def main():
    init()
    player2 = randint(1,3)
    player1 = int(input('selection:'))
    
    fight(player1, player2) 
    input('')


    return 0

main()