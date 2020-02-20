'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

salary_average = []

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        salary = line.split()
        salary_average.append(int(salary[1]))
        if int(salary[1]) < 20000:
            print(salary[0])
    print(sum(salary_average) / len(salary_average))
