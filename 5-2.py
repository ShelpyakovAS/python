'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

lines = 0
words = 0

with open('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lines += 1
        words += len(line.split())

print("Строк:", lines)
print("Слов:", words)