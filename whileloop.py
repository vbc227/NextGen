import random
# secret_num= random.randint(1,10)
# guess=int(input('Guess number 1-10:'))
# while guess != secret_num:
#     if guess>secret_num:
#         print('Too High.', end='')
#     else:
#         print('Too Low', end='')
#     guess = int(input('Wrong. Guess number 1-10:'))
# # guess= int(input('Guess number 1-10:'))
# print(secret_num)
# print('you are correct finally!!')
user_guess=1
print('Im thinking of a number 1-10 are you ready to guess')
user_input=input('Is it' +  str(random.randint(1,10)))
while user_input.lower()!='yes'and user_guess<=3:
    user_input=input('Is it' + str(random.randint(1,10)))
    user_guess= user_guess+1
    print(user_guess)
print('I win')


