my_dict = {'Вася': 1999, 'Петя': 1994, 'Миша': 2012, 'Сережа': 2021}
print("Dictionary:", my_dict)
print("Existing value:", my_dict['Петя'])
print("Not existing value:", my_dict.get('Саша'))
my_dict.update({'Оля': 1985,
                'Наташа': 1974})
b = my_dict.pop('Сережа')
print("Deleted value:", b)
print("Modified dictionary:", my_dict)

my_set = {1,4,3,2,1,0,2,3,4,5,7,8,2.2, False, 'Moonlight', (1,2,4,3)}

print ("Set:", my_set)
other_set = (15,22)
my_set = my_set.union(my_set, other_set)
print(my_set.remove(4))
print ("Modified set", my_set)
