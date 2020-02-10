# 3. Пользователь вводит месяц в  виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
user_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
your_month = {1: 'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето',
              7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'
}
print(your_month[user_month])

user_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
your_month = ['Зима', 'Весна', 'Лето', 'Осень']

if user_month == 1 or user_month == 2 or user_month == 12:
    print(your_month[0])
elif user_month == 3 or user_month == 4 or user_month == 5:
    print(your_month[1])
elif user_month == 6 or user_month == 7 or user_month == 8:
    print(your_month[2])
elif user_month == 9 or user_month == 10 or user_month == 11:
    print(your_month[3])