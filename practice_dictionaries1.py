residents={'Puffins':104,'Sloth': 105,'Burmese Python' :106}
menu={}
menu['Sunday']=16.78
print(menu['Sunday'])
menu['Monday']=3
menu['Tuesday']=0

print(menu)
for key in menu:
    print(key, ':', menu[key])
#key - animals_name : value - location
zoo_animals= {'unicorn': 'cotton candy house',
'sloth':'Rainforest Exhibit',
'Bengal Tiger': 'Jungle House',
'Atlantic Puffin' :'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit',}
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
for k in zoo_animals:
    print(k, ":", zoo_animals[k])
#5
my_dict={'title': 'stranger Things', 'is_snow':True, 'seasons':2}
print(my_dict.items())

