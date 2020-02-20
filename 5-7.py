'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
firm_1 ООО 56000 22000
firm_2 ОАО 14000 4000
firm_3 АО 25000 12000
firm_4 ООО 22000 7000
firm_5 ООО 2000 7000
firm_6 ООО 5000 7000
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
'''
import json
all_profit = 0
dict1 = {}
with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines = line.split()
        print(f'Прибыль {lines[1]} "{lines[0]}": {int(lines[2]) - int(lines[3])}')
        dict1.update({lines[0]: (int(lines[2]) - int(lines[3]))})
        if int(lines[2]) - int(lines[3]) > 0:
            all_profit = all_profit + int(lines[2]) - int(lines[3])
    print(f'Суммарная прибыл за вычитом убыточных: {all_profit}')
my_list = [dict1]
print(my_list)
with open('test.json', 'w', encoding='utf-8') as test:
    json.dump(my_list, test)