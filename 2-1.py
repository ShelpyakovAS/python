# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [33, 'table', 48, 4.96, 'war', 777, 'qwerty', '475', 'ddddd']
i = 0
while i < len(my_list):
    print(f'{my_list[i]} = {type(my_list[i])}')
    i = i + 1