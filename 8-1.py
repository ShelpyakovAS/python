import random


def take_card(card):
    barrels = [i for i in range(1, 91)]
    for j in range(len(card)):
        i = 0
        while i != 5:
            barrel = random.choice(barrels)
            barrels.remove(barrel)
            card[j].append(barrel)
            i += 1


def barral_in_card(card):
    error = 0
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == barrel:
                card[i].insert(j, '-')
                card[i].remove(barrel)
            else:
                error += 1
    return error


def check_answer(card):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == barrel:
                print('Вы проиграли!!!')
                return 'сдаюсь'


def check_win(card):
    win = 0
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == '-':
                win += 1
    return win



user_card = [[], [], []]
comp_card = [[], [], []]
barrels = [i for i in range(1, 91)]
user_answer = 0
take_card(user_card)
take_card(comp_card)

while user_answer != 'сдаюсь' or len(barrels) == 1:
    barrel = random.choice(barrels)
    barrels.remove(barrel)
    print(f'Новый боченок: {barrel} (осталось {len(barrels) -1})')
    print(f'Ваша карточка: {user_card}')
    print(f'Компьютера карточка: {comp_card}')
    user_answer = input('Зачеркнуть цифру на карточке или продолжить: ')
    if user_answer.lower() != 'зачеркнуть' and user_answer.lower() != 'продолжить':
        print('Нужно ввести зачеркнуть или продолжить!')
        user_answer = input('Зачеркнуть цифру на карточке или продолжить: ')
    if user_answer.lower() == 'зачеркнуть':
        if barral_in_card(user_card) == 15:
            print('Вы проиграли!!!')
            user_answer = 'сдаюсь'
        else:
            barral_in_card(user_card)
    elif user_answer.lower() == 'продолжить':
        user_answer = check_answer(user_card)
    barral_in_card(comp_card)
    if check_win(user_card) == 15:
        print('Вы выйграли!!!')
        user_answer = 'сдаюсь'
    if check_win(comp_card) == 15:
        print('Компьютер выйграл!!!')
        user_answer = 'сдаюсь'

