import random as rm
import os

# Make your game type hear
a = 'st'
b = 'p'
c = 'sr'

logFn = 'score.log'

if not os.path.exists(logFn):
    with open(logFn) as lf:
        lf.write(str(0))

with open(logFn) as s2:
    i = int(s2.read())

def gameWin(comp, you):
	if comp==you:
		return 'N'
		
	elif comp==f'{a}':
		if you==f'{b}':
			return 'T'
			
		elif you==f'{c}':
			return 'F'
		
	elif comp==f'{b}':
		if you==f'{c}':
			return 'T'
			
		elif you==f'{a}':
			return 'F'
		
	elif comp==f'{c}':
		if you==f'{a}':
			return 'T'
			
		elif you==f'{b}':
			return 'F'
			


T = 0
count = 1

while (T!=2):
    T = T + 1
    player = input(f"\nEnter your name: ").strip().capitalize()
    print(f"\nPlayer No.{count}: ", end='')
    print(player)
    print('')
    you = input(f"💎({a}), 📃({b}), ✌️({c}): ").lower().strip()
    
    
    print("Computer's turn: ", end="")
    rmNo = rm.randint(1,3)
    
    if rmNo>=0:
        print('selected')
    
    else:
        print('wating...')
    
    
    if rmNo==1:
        comp=f'{a}'
    
    elif rmNo==2:
	       comp=f'{b}'
    
    elif rmNo==3:
        comp=f'{c}'
    
    
    result = gameWin(comp, you)
    
    print(f"\nComputer selected: {comp}")
    print(f"You selected: {you}")
    print('')
    print(f"        | The results of {player}'s turn is below: |")
    print('')
    space1= '           '
    space2= '            '
    space3= '           '
    
    
    if result=='T':
        print(f"{space1}***{player}, You win!🎆🎉😘***")
        r = 'T'
    elif result=='F':
        print(f"{space2}***You Lose!😅😅😧***")
        r = 'F'
    elif result=='N':
        print(f"{space3}***@@ The game tie @@***")
        r = 'N'
    
    if r=='T':
        i= i+1
        with open(logFn, 'w') as s:
            s.write(f'{i}')
    
    
    print(f'\nYour Score: {i}')
    count = count + 1
    print('')
    print('-----------------------------------')
    print('')