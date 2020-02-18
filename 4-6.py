'''
6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''
from itertools import cycle, count


def my_func1(i):
    for al in count(i):
        print(al)




def my_func2(i):
    for al in cycle(i):
        print(al)


# my_func1(1)
# my_func2('wqe')
