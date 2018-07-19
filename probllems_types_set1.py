import random
import time
print(int(2.9))
print(int(-2.5))
#year = input('Year of Birth:')
# print(2018-int(year))
#3
a=3
b=5
c=7
# print True if a< b and b<d # also point True if a>b and b>c
print (a<b and b<c)
# OR print True if a>b and b>c
print (a>b and b>c)
#4
year=random.randint(1000,2018)
#use % to see if year is divisble by 4
# #unless it is divisible by 100
# it's ok to be divisible by 100 if also divisible by 400
print (year% 4==0 and year% 100!=0 or year% 400==0)
print ('was',year,'a leap year?')
print(random.choice(('dog','cat', 'lizard')))

