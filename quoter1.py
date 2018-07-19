# import re
#file = open("ZC:/Users/Valentina Barragan/Desktop/harrypotter.txt",'r')
try:
    file = open("ZC:/Users/Valentina Barragan/Desktop/harrypotter.txt", 'r')

    text = file.read()
    file.close()
except:
    pass
print('rest of code')
#
# text=file.read()
# file.close()
# print(text[:1000])
# harry_quotes=re.findall('.*Harry.*', text)
# for quote in harry_quotes:
#     print(quote)
# print(len(harry_quotes))

# title=['the tale of two cities', 'wind in the willows', 'gone with the wind', 'about a boy']
# title=str(title).list()
# print(nlist)
# def fix_title(title):
#     fixed_title=title.lower()
#     fixed_title=title.capitalize()
#     nlist=fixed_title.split()
#     for x in range(len(nlist)):
#         if nlist[x]not in ('a','and','or'):
#             nlist[x]=nlist[x].capitalize()
#     fixed_title=' '.join(nlist)
#     return fixed_title
# print (fix_title('GONE WITH THE WIND'))
