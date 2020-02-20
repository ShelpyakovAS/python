'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
 При этом английские числительные должны заменяться на русские.
 Новый блок строк должен записываться в новый текстовый файл.
'''

dict1 = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
help_file = []
with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split()
        help_file.append(f'{dict1[int(lines[2])]} {lines[1]} {lines[2]}')
with open('text.txt', 'w', encoding='utf-8') as f:
    for i in help_file:
        f.write(i+'\n')