'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
user_say = input('Введите числа через пробел: ')
result = 0
with open('text.txt', 'w', encoding='utf-8') as f:
    while user_say != '':
        f.write(user_say + '\n')
        user_say = input('Введите числа через пробел: ')

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split()
        for i in lines:
            result = result + int(i)

print(result)
