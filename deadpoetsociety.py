import random
with open("C:/Users/Valentina Barragan/Desktop/dead_poets_final.txt",'r') as f:
    text=f.read()
text=text.replace('.','').replace('?','').replace('!','').replace(',','')

text_list=text.split()
print(len(text_list))
unique_list=list(set(text_list))
print (len(unique_list))
print ('Nolan appears', text_list.count('NOLAN'), 'times')
rword=random.choice(unique_list).lower()
for r in rword:
    print('_ ', end='')
all_guesses=[]
print()#new empty line
turn=0
while turn<10:
    player_letter=input('Guess a letter from Dead Poets Society')
    turn=turn+1 #count the turn
    if player_letter in rword:
         print('correct!')

    all_guesses.append(player_letter)
    for r in rword:
        if r in all_guesses: #show letter they guessed
            print(r,end='')
        else:
            print('- ', end='') #hide letters they haven't guessed
print(rword)