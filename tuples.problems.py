# text= 'How are you today good sir? I Hope you are well'
# text_tuple=tuple(text.split())
# print (text_tuple)
# print('There are', len(text_tuple),'words')
# text=text.replace('?', '')
# text= text.replace('p','')
# names=('Kathy','lina','Michi','Ale')
# for n in names:
#     print('there are', len(n),'letters
import random
num_names=int(input('How many names?'))
for n in range(num_names):
    firstname= ('Nina','Feicia','Vale','Vanessa')
    lastname=('Barragan','Martinez','Gomez', 'Daniels')
    print(random.choice(firstname), random.choice(lastname))
