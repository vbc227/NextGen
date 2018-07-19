things=['camera', 'couch', 'potato salad', 'energy drink', 'comb','suitcase']
price= [50,100,5,5,1,25]
for w in range(len(things)):
    print('{:>12}: ${:>6.2f})'.format(things[w],price[w]))

