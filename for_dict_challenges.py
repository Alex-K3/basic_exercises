# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
from collections import Counter
from tokenize import group

from pytest import Item

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
names = []
for student in students:
    for atr, name in student.items():
        names.append(name)
for name, count in Counter(names).items():
    print(f'{name}: {count}')
print()
  


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
names = []
counts = 0
name1 = ''
for student in students:
    for atr, name in student.items():
        names.append(name)
for name, count in Counter(names).items():
    if counts < count:
        counts = count
        name1 = name
    else:
        continue
print(f'Самое часток имя среди учеников: {name1}')
print()


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
group = 0
for students in school_students:
    group += 1
    names = []
    counts = 0
    name1 = ''
    for student in students:
        for atr, name in student.items():
            names.append(name)
    for name, count in Counter(names).items():
        if counts < count:
            counts = count
            name1 = name
        else:
            continue
    print(f'Самое часток имя в классе {group}: {name1}')
print()


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for number_of_classes in school:
        name_class = number_of_classes['class']
        count_m = 0
        count_f = 0
        for names in number_of_classes['students']:
            name_students = names['first_name']
            if is_male[name_students] == True:
                count_m += 1
            else:
                count_f += 1
        print(f'Класс {name_class}: девочки {count_f}, мальчики {count_m}')
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

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

for number_of_classes in school:
        name_class = number_of_classes['class']
        count_m = 0
        count_f = 0
        for names in number_of_classes['students']:
            name_students = names['first_name']
            if is_male[name_students] == True:
                count_m += 1
            else:
                count_f += 1
        if count_m > count_f:
            print(f'Больше всего мальчиков в классе {name_class}')
        else:
            print(f'Больше всего девочек в классе {name_class}')

