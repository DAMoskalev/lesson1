# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
# ???
print('Задание 1:')

stud_list = []
for i in students:
    stud_list.append(i.get('first_name'))

stud_list.sort()

buf = ''
for i in stud_list:
    if buf != i:
        print('{} {} раз'.format(i, stud_list.count(i)))
        buf = i

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Ваня'},
]

print('\nЗадание 2:')

stud_list = []
for i in students:  # список учеников
    stud_list.append(i.get('first_name'))

stud_list.sort()


def max_entry(s_list):
    count = 0
    for i in s_list:  # максимальное количество совпадений
        if s_list.count(i) > count:
            count = s_list.count(i)
    result_list = []
    for i in s_list:
        if s_list.count(i) == count:
            if '{} {}'.format(i, count) not in result_list:
                result_list.append('{} {}'.format(i, count))
    return result_list


for i in max_entry(stud_list):
    print(i)
# ???

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ]
]
# ???
print('\nЗадание 3:')

for i in school_students:
    stud_list = []
    for j in i:
        stud_list.append(j.get('first_name'))
    for j in max_entry(stud_list):
        print(j)

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print('\nЗадание 4:')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for i in school:
    male = 0
    female = 0
    for j in i.get('students'):
        if is_male.get(j.get('first_name')):
            male += 1
        else:
            female +=1
    print('В классе {} {} девочек и {} мальчиков'.format(i.get('class'), female, male))


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
print('\nЗадание 5:')
for i in school:
    m_count = 0
    f_count = 0
    for j in i.get('students'):
        if is_male.get(j.get('first_name')):
            m_count += 1
        else:
            f_count += 1
    i['m_count'] = m_count
    i['f_count'] = f_count

f_max = ''
m_max = ''
f_tmp = 0
m_tmp = 0
for i in school:
    if int(i.get('m_count')) > m_tmp:
        m_tmp = int(i.get('m_count'))
        m_max = i.get('class')
    if int(i.get('f_count')) > f_tmp:
        f_tmp = int(i.get('f_count'))
        f_max = i.get('class')
print('Девочек больше в {}'.format(f_max))
print('Мальчиков больше в {}'.format(m_max))

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
