user_input=input("Would you like to apply for a job?")
no='goodbye!'
yes='Do you have job experience?'
if user_input == "no":
    print(no)
elif user_input == 'yes':
    second_user_input=input('Do you have job experience?')
    if second_user_input=='no':
        print('You may apply for an entry-level position?')
    elif second_user_input=='yes':
        third_user_input=int(input('How many years?'))
        if third_user_input>3:
            print('You may apply for an advanced position!')
        elif third_user_input<=3:
            print('You may apply for a mid-level position')
# # user_input=input('Are you hungry?')
# # second_user_input=input('Do you have money?')
# # if user_input=='yes'and second_user_input=='yes':
# #     print('Here is a take-out menu')
# # elif user_input=='yes'and second_user_input=='no':
# #     print('Time to heat up leftovers')
# # if user_input=='no' and second_user_input=='yes':
# #         print('Buy yourself something nice')
# # if user_input=='no' and second_user_input=='no':
# #     print("Let's read a book!")
import random
dice_one= random.randint(1,6)
dice_two= random.randint(1,6)
print(dice_one)
print(dice_two)
if dice_one == dice_two or dice_one +dice_two==6 or dice_one + dice_two==3:
    print('you win!')