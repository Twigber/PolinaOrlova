# Python HW 5 Functions, Lists
#  - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению)
#  - Все результаты выводить в консоль.
#
# Написать скрипт который в создаст список целых чисел.
import random
import datetime, randomtimestamp
from string import ascii_letters
import russian_names

list_int = list(range(1, 71))
print('list_int =', list_int)

# Написать скрипт который в создаст список целых чётных чисел.
print('==========================')
list_int_even_create = list(range(0, 70, 2))
print('list_int_even_create =', list_int_even_create)

# Написать скрипт который в создаст список целых нечётных чисел.
print('==========================')
list_int_odd_create = list(range(1, 70, 2))
print('list_int_odd_create =', list_int_odd_create)

# Написать скрипт который из списка целых чисел выведет чётные числа.
print('==========================')
list_int_even = []
for i in list_int:
    if i % 2 == 0:
        list_int_even.append(i)

print('list_int_even =', list_int_even)

# Написать скрипт который из списка целых чисел выведет нечётные числа.
print('==========================')
list_int_odd = []
for i in list_int:
    if i % 2 == 1:
        list_int_odd.append(i)
print('list_int_odd =', list_int_odd)

# Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
print('==========================')
list_int_even_5 = []
for i in list_int:
    if i % 5 == 0:
        list_int_even_5.append(i)

print('list_int_even_5 =', list_int_even_5)

# Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
print('==========================')
list_int_even_5 = []
for i in list_int:
    if i % 5 == 0:
        list_int_even_5.append(i)

print('list_int_even_5 LEN=', len(list_int_even_5))

# Написать скрипт который в создаст список целых рандомных чисел.
print('==========================')
list_int_random = []
rand = 20

for i in range(rand):
    a = random.randint(1, 70)
    list_int_random.append(a)

print('list_int_random =', list_int_random, len(list_int_random))


# Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
print('==========================')

def polina (list, n):
    list_int_5 = []
    while len(list) > n:
        pice = list[:n]
        list_int_5.append(pice)
        list = list[n:]
    list_int_5.append(list)
    print('list_int_5 =', list_int_5)
    print('pice =', pice)
    print('list =', list)
    # return list_int_5


polina(list_int, 5)



# Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел.
print('==========================')
def polina_2 (list):
    list_int_odd_2 = []
    list_int_even_2 = []
    for i in list:
        if i % 2 == 0:
            list_int_even_2.append(i)
        else:
            list_int_odd_2.append(i)
    print('list_int_odd_2 =', list_int_odd_2)
    print('list_int_even_2 =', list_int_even_2)


polina_2(list_int)

# Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
print('==========================')
stars_5 = []
for i in range(70):
   a = []
   for n in range(5):
       if len(a) < 5 :
           c = random.randint(1, 100)
           a.append(c)
       if len(a) == 5 :
           stars_5.append(a)


print('stars_5 =', stars_5, len(stars_5))



# Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars
print('==========================')

stars_5 = []
for i in range(70):
   a = []
   for n in range(5):
       if len(a) < 5 :
           c = random.randint(1, 100)
           a.append(c)
       if len(a) == 5 :
           a = sum(a)
           stars_5.append(a)



print('stars_5 =', stars_5, len(stars_5))

# Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка.
# В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
print('==========================')
def polina_2 (list_stars_5):
    list1 = []
    list2 = []
    for i in list_stars_5:
        if i > 100 or i == 100:
            list1.append(i)
        if i < 100:
            list2.append(i)
    if len(list1) >= 1:
        print('Больше 100 =', list1)
    if len(list2) >= 1:
        print('Меньше 100 =', list2)
    if len(list1) == 0:
        print('Больше 100 =', 'No lists')
    if len(list2) == 0:
        print('Меньше 100 =', 'No lists')


polina_2(stars_5)

# Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
print('==========================')
def polina_3 ():
    age = int(input('Сколько вам лет:'))
    salary = int(input('Сколько вы зарабатываете в месяц ($):'))
    part_of_the_salary = int(input('Какой процент вашего заработка вы готовы откладывать ежемесячно:'))
    saving_money_every_month = salary / 100 * part_of_the_salary
    print('Каждый месяц вы откладываете =', saving_money_every_month, '$')
    dreams = int(input('Сколько бы вы хотели накопить($):'))
    reality_month = dreams / saving_money_every_month
    print('Вы закончите копить через: ', reality_month, 'месяцев')
    reality_year = reality_month // 12
    print('Это =', reality_year, 'лет')
    your_dream_age = age + reality_year
    print('Вам будет:', your_dream_age, 'лет')
    if your_dream_age>90:
        print('Вам желательно копить быстрее, что бы успеть воспользоваться этими деньгами')
    if your_dream_age<90 and your_dream_age>60:
        print('Ура! Торопитесь скорее потратить ваши деньги!')
    if your_dream_age<60:
        print('Вы великолепны')


# polina_3()
# Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа.
# Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of function body logic
print('==========================')

def polina_4 ():
    salary_start = int(input('Заработная плата Junior QA на старте:'))
    work_exp = int(input('Сколько лет вы работаете в компании:'))
    work_exp_up_every_year = 1.3
    n = [salary_start]
    for i in range(work_exp):
        z = n[-1] * work_exp_up_every_year
        n.append(z)
    salary_after_up = n[-1]
    postman = str(input('Обладаете ли Вы навыками работы в Postman (да или нет):'))
    sql = str(input('Знаете ли Вы SQL(да или нет):'))
    android_studio = str(input('Обладаете ли вы навыками тестирования мобильных приложений(да или нет):'))
    git_bash = str(input('Обладаете ли вы навыками работы в терминале Linux (да или нет):'))
    if postman == 'да' or postman == 'yes':
        p = n[-1] * 1.1
        n.append(p)
    if sql == 'да' or sql == 'yes':
        s = n[-1] * 1.1
        n.append(s)
    if android_studio == 'да' or android_studio == 'yes':
        a = n[-1] * 1.1
        n.append(a)
    if git_bash == 'да' or git_bash == 'yes':
        g = n[-1] * 1.1
        n.append(g)


    print('Ваша ЗП с учетом вашего опыта =', n[-1], '$')
# polina_4()







# Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
print('==========================')
import names

list_user_name = []
for i in range(70):
    user_name = names.get_full_name()
    list_user_name.append(user_name)
print('list_user_name =', list_user_name, len(list_user_name))

# Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер.
print('==========================')

fales = ['file_%s'%y for y in range(70)]
print('fales =', fales, len(fales))
#=========================================ГЕНЕРАТОРЫ===================================================================
def generate_family():
    family = [True, False]
    family_random = random.sample(family, 1)
    family_random = family_random[0]
    return family_random

def russian_people ():
    rn = russian_names.RussianNames(count=1, patronymic=False, name_reduction=False)
    z = rn.get_batch()
    z = z[0]
    return z

def generate_password():
    password = ''
    for i in range(8):
        password += random.choice(ascii_letters)
    return password

def generate_login():
    login = ''
    for i in range(5):
        login += random.choice(ascii_letters)
    return login

def generate_email():
    email = ''
    for i in range(7):
        letter = random.sample(ascii_letters, 1)[0]
        email += letter
    email+='@gmail.com'
    return email

def generate_salary():
    s = random.randint(300, 5000)
    return s

#======================================================================================================================

#  Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.
print('==========================')

list_name_date = []
i = 0
while i < 70:
    d = randomtimestamp.random_date()
    n = russian_people()
    list_name_date_m = []
    list_name_date_m.append(n)
    list_name_date_m.append(d)
    list_name_date.append(list_name_date_m)
    i += 1

print('list_name_date =', list_name_date, len(list_name_date))

# Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором:
# 0-й - элемент - это имя пользователя,
# 1-й - элемент - это логин,
# 2-й - элемент - это пароль,
# 3-й - элемент - это email (email тоже генерировать),
# 4-й - элемент - это дата регистрации
print('==========================')

employees = []

for i in range(len(list_name_date)):
    name = list_name_date[i][0]
    login = generate_login()
    password = generate_password()
    user_email = generate_email()
    date = list_name_date[i][1]
    mini_employees = []
    mini_employees.append(name)
    mini_employees.append(login)
    mini_employees.append(password)
    mini_employees.append(user_email)
    mini_employees.append(date)
    employees.append(mini_employees)

print('Employees =', employees)

# Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - семейный статус (True, False - генерировать рандомно),
print('==========================')


family = []
for i in range(len(employees)):
    l = employees[i][1]
    n = employees[i][0]
    f = generate_family()
    mini_family = []
    mini_family.append(l)
    mini_family.append(n)
    mini_family.append(f)
    family.append(mini_family)
print('Family =', family)

# Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - гендер (1-м, 0-ж)
print('==========================')

gender = []
for i in range(len(family)):
    l = family[i][0]
    n = family[i][1]
    if n[-1] == 'н' or n [-1] == 'в' or n [-1] == 'й':
        g = 1
    else:
        g = 0
    mini_gender = []
    mini_gender.append(l)
    mini_gender.append(n)
    mini_gender.append(g)
    gender.append(mini_gender)
print('gender =', gender)

# Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором:
# 0-й - элемент - это логин,
# 1-й - элемент - это имя,
# 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
print('==========================')

salary = []
for i in range(len(family)):
    l = family[i][0]
    n = family[i][1]
    s = generate_salary()
    miny_salary = []
    miny_salary.append(l)
    miny_salary.append(n)
    miny_salary.append(s)
    salary.append(miny_salary)
print('salary =', salary)

# Написать скрипт который создаст список имён работников из salary у которых ЗП от 1500$ до 3000$
print('==========================')

salary_1500_3000 = []

for i in range(len(salary)):
    if salary[i][2]>1500 and salary[i][2]<3000:
        salary_1500_3000.append(salary[i][1])
print('salary_1500_3000 names =', salary_1500_3000)

# Написать скрипт который создаст список имён мужчин из gender.
print('==========================')

male_gender = []
for i in range(len(gender)):
    if gender[i][2] == 1:
        male_gender.append(gender[i][1])
print('male_gender =', male_gender)

# Написать скрипт который создаст список имён женщин из gender.
print('==========================')

female_gender = []
for i in range(len(gender)):
    if gender[i][2] == 0:
        female_gender.append(gender[i][1])
print('female_gender =', female_gender)

# Написать скрипт который создаст список имён неженатых мужчин из family.
print('==========================')

family_false_male = []
for i in range(len(family)):
    if family[i][2] == False:
        family_false = []
        family_false.append(family[i][1])
        for y in range(len(family_false)):
            if family_false[y][-1] == 'н' or family_false[y][-1] == 'в' or family_false[y][-1] == 'й' or family_false[y][-1] == 'х':
                family_false_male.append(family_false[y])
print('family_false_male =', family_false_male)

# Написать скрипт который создаст список имён незамужних женщин из family.
print('==========================')

family_false_female = []
for i in range(len(family)):
    if family[i][2] == False:
        family_false = []
        family_false.append(family[i][1])
        for y in range(len(family_false)):
            if family_false[y][-1] == 'а' or family_false[y][-1] == 'я':
                family_false_female.append(family_false[y])
print('family_false_female =', family_false_female)

# Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций
print('==========================')
norm_mans_script = []
for i in range(len(family)):
    if family[i][2] == False:
        for q in range(len(gender)):
            if gender[q][2] == 1:
                for s in range(len(salary)):
                    if salary[s][2]>=1500:
                        if family[i][1] == gender[q][1] == salary[s][1]:
                            norm_mans_script.append(family[i][1])
print('Свободные мужики с нормальными зарплатами =', norm_mans_script)


# Реализуйте пункт 28 через через функции.
print('==========================')


def norm_mans_def():
    norm_mans = []
    for i in range(len(family)):
        if family[i][2] == False:
            for q in range(len(gender)):
                if gender[q][2] == 1:
                    for s in range(len(salary)):
                        if salary[s][2] >= 1500:
                            if family[i][1] == gender[q][1] == salary[s][1]:
                                norm_mans.append(family[i][1])
    print('Свободные мужики с нормальными зарплатами (результат функции) =', norm_mans)


norm_mans_def()

# Поешьте и выспитесь)
