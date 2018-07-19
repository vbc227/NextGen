import random
#main_course_list= ['steak','salmon','rice']
# main_course_list.insert(0,'stew')
# print(main_course_list)
#2
main_course_list= ['stew','steak','salmon','rice']
user_input= input('Type at least 3 main courses')

new_meal=main_course_list.extend(['burger','tilapia','gulash'])
print('Ok these are the new main courses', main_course_list)
#3
sides_list=['carrots','fries','salad']
style_list=['seared', 'boiled','baked']
print('Tonight I will serve', random.choice(style_list), random.choice(main_course_list),'with', random.choice(sides_list))
#calculator
problem=input('enter a problem, example 1+2:')
plist=problem.split()
print(plist)
a= int(plist[0])
b=int(plist[2])
operator= plist[1]
if operator=='+':
    print(a+b)
elif operator=='-':
    print (a-b)
elif operator=='*':
    print(a*b)
elif operator=='/':
    print(a/b)
else:
    print ('unknown operator')x