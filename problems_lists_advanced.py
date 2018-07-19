import random
#alist=['hat','cat','book']
# for a in range(len(alist)):
#     alist[a]= alist[a]+'s'
#     print(alist[a])
# #2
# nums=[1,2,3,4,5,6]
# for n in range(len(nums)):
#     nums[n]=nums[n]**2
#     print(nums[n])
# #3
# weights=[['dog',30], ['mug',2],['book',4]]
# for w in weights:
#      print(w)
#
# for w in range(len(weights)):
#     print('A', weights[w][0], 'weighs',weights[w][1], 'pounds')
# # print(weights[1])
# weights.append(['truck',5000])
# print(weights)
# for w in range(len(weights)):
#     print('A', weights[w][0], 'weighs',weights[w][1], 'pounds')
# #set 2
targets=['0','0','0','0','0','0','0','0','0','0']
for x in targets:
    print(x,end=' ')
prize_spot=random.randint(0,len(targets))
player_guess=-1
guess=int(input("guess prize spot here"))
turns=0
while player_guess!=prize_spot:
    player_guess=int(input('\nGuess which spot I hid the prize:\n'))
    turns +=1
    if player_guess!= prize_spot:
        print('wrong!')
        targets[player_guess]='x'
    else:
        targets[player_guess]='!!@!!'
    #print the board nicely
    for x in targets:
        print(x, end=' ')
print('\nYou win!!!')
