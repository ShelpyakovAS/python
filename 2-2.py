# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = [33, 'table', 48, 4.96, 'war', 777, 'qwerty', '475', 'ddddd']
i = 0
while i < len(my_list) - 1:
    exchanger = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = exchanger
    i = i + 2
print(my_list)