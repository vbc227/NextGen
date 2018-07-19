# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
file = open("C:/Users/Valentina Barragan/Desktop/harrypotter.txt",'r')
text=file.read()
text= text.lower()
text= text.replace(',','')
# print(text)
text_list=text.split()
#for line in file:
 #   print(line)
 #same way to the action above
file.close()
#3 technique #you dont need file.close this way
with open("C:/Users/Valentina Barragan/Desktop/harrypotter.txt",'r') as file:
    text=file.read()
set_list=set(text_list)
print ((len(text_list)))
print (len(set_list))
#print how many unique words
print(len(set(text_list)))
unique_list=list(set(text_list)) #turn unique set to a list
# print(random.choice(unique_list))
# print(text_list,'appears'text_list.count(text_list))
fo=open("C:/Users/Valentina Barragan/Desktop/hp_wordcounts.txt",'w')
for w in unique_list:
    print(w,'appears', text_list.count(w),file=fo)
adverbs=[w for w in unique_list if w.endswith('ly')]
hyphenated=[w for w in unique_list if '-' in w]
s_words=[w for w in unique_list if w.startswith('s')]
gerunds=[w for w in unique_list if w.endswith('ing')]
cap_names=[w.capitalize() for w in unique_list if w in ('harry','ron', 'hermione')]
print(adverbs)
print(hyphenated)
print(s_words)
print(unique_list)
fo.close()

plt.plot(['total words','unique words'],[len(set_list),len(unique_list)])



