# Создать переменную типа String
name = 'Polina'

# Создать переменную типа Integer
age = 32

# Создать переменную типа Float
sons_age = 4.11

# Создать переменную типа Bytes
sons_name = b"Mitya"
sons_age2 = bytes(4)


# Создать переменную типа List
name_list = list('Polina')


# Создать переменную типа Tuple
sons_name_tuple = tuple('Mitya Orlov')


# Создать переменную типа Set
husbands_name = set('Alexander')


# Создать переменную типа Frozen set
husbands_name2 = frozenset('Alexander')


# Создать переменную типа Dict
d = {'name':'Polina', 'age': 32}

s = dict(name = 'Mitya', age = 4.11)


# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(type(name))
print(type(age))
print(type(sons_age))
print(type(sons_name))
print(type(sons_age2))
print(type(name_list))
print(type(sons_name_tuple))
print(type(husbands_name))
print(type(d))
print(type(s))

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
pets_dog = 'Bella'
pets_cat = 'Marfa'
pets = pets_cat + pets_dog
print(pets)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
bellas_age = 11
dog = pets_dog, bellas_age
print(dog)

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
marfa_age = 3
cat = pets_cat + str(marfa_age)
print(cat)