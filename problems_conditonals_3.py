# user_input=int(input('What did you get on the test?'))
# if user_input>=93:
#     print('A+')
# elif user_input>=90:
#      print('A-')
# elif user_input>=87:
#     print('B+')
# elif user_input>=85:
#     print('B')
# elif user_input>=83:
#     print('B-')
operand_one= int(input('Enter OPERAND:'))
operator=input('Enter + or -')
operand_two=int(input('Enter operand:'))
if operator=='+':
    print(operand_one+operand_two)
elif operator=='-':
    print(operand_one - operand_two)
else:
    print('Cant recognize the operator')
