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
for name in set(names):
    print(f'{name}: {names.count(name)}')
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
name_user = ''
for student in students:
    for atr, name in student.items():
        names.append(name)
for name in set(names):
    if names.count(name) > counts:
        print(names.count(name))
        counts = names.count(name)
        name_user = name
    else:
        continue
print(f'Самое часток имя среди учеников: {name_user}')
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
    name_user = ''
    for student in students:
        for atr, name in student.items():
            names.append(name)
    for name in set(names):
        if names.count(name) > counts:
            counts = names.count(name)
            name_user = name
    print(f'Самое часток имя в классе {group}: {name_user}')
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

def male(name, count_m, count_f):
    male_name = is_male[name]
    if male_name:
        count_m += 1
    else:
        count_f += 1
    return count_m, count_f

def school_class(total_school):
    for number_of_classes in total_school:
        name_class = number_of_classes['class']
        count_m = 0
        count_f = 0
        result = []
        for names in number_of_classes['students']:
            name_students = names['first_name']
            count_m, count_f = male(name_students, count_m, count_f)
            result.append(f'Класс {name_class}: девочки {count_f}, мальчики {count_m}')
    return result


if __name__ == '__main__':
    res = school_class(school)
    for item in res:
        print(item)
print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
    'Даша': False,
}

max_male = {'class_name': '', 'male': 0}
max_female = {'class_name': '', 'female': 0}
for number_of_classes in school:
        name_class = number_of_classes['class']
        count_m = 0
        count_f = 0
        for names in number_of_classes['students']:
            name_students = names['first_name']
            if is_male[name_students]:
                count_m += 1
            else:
                count_f += 1
        if count_m > max_male['male']:
            max_male['male'] = count_m
            max_male['class_name'] = name_class
        if count_f > max_female['female']:
            max_female['female'] = count_f
            max_female['class_name'] = name_class


print(f'Больше всего мальчиков в классе {max_male["class_name"]}')
print(f'Больше всего девочек в классе {max_female["class_name"]}')


