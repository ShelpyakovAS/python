'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
'''
generator = (88, 66, 57, 52, 66, 5, 7, 9, 77, 64, 52)
my_list = []
my_list.append(generator[0])
for index, item in enumerate(generator):
    if index + 1 > len(generator) -1:
        break
    elif generator[index + 1] > generator[index]:
        my_list.append(generator[index + 1])




print(my_list)
