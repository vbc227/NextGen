import vars

t=9
name='Mr.T'
animal= 'hippo'
print(vars())
d= vars().copy() #save as variable
print(d.items()) #a list of tuples
for k, v in d.items():
    print(k,":", v)
#option 1
for k in d:
    if '_' not in k:
        print(k,':', d[k])
#print the values