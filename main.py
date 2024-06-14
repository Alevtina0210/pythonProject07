my_dict = {'Alevtina': 1968, 'Alexandr': 1961}
print(my_dict)
print(my_dict.get('Alevtina'))
print(my_dict.get('Semen'))
my_dict.update({'Ekaterina': 1988, 'Rostislav': 1989})
print(my_dict)
my_dict.pop('Alexandr')
print(my_dict)

my_set = {3, 4, 5, 3, 6.5, True, 6.5, 'Summer'}
print(my_set)
my_set.add(8)
print(my_set)
my_set.remove('Summer')
print(my_set)
