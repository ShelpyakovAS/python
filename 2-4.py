# 4. Пользователь вводит строку из  нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

user_str = input('Вводите строку из нескольких слов, разделённых пробелами: ')
user_list = user_str.split()
print(user_list)
i = 0
while i < len(user_list):
    if len(user_list[i]) >= 10:
        len_numb = len(user_list[i]) - 10
        print(f'{i + 1}. {(user_list[i])[:len(user_list[i]) - len_numb]}')
        i = i + 1
    else:
        print(f'{i+1}. {user_list[i]}')
        i = i + 1