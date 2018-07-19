from random import randint
winning_number= randint(1,2)
message='you win!'
user_input= int(input('Enter a guess'))
if user_input> winning_number:
    message='too high'
elif user_input < winning_number:
    message= 'too low!'
print (message)

print(winning_number)



