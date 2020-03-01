import random


class Card:
    def __init__(self, card):
        self.card = card

    def __str__(self):
        return f'{self.card}'

    def take_card(self):
        barrels = [i for i in range(1, 91)]
        for j in range(len(self.card)):
            i = 0
            while i != 5:
                barrel = random.choice(barrels)
                barrels.remove(barrel)
                self.card[j].append(barrel)
                i += 1

    def barral_in_card(self):
        error = 0
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if self.card[i][j] == barrel:
                    self.card[i].insert(j, '-')
                    self.card[i].remove(barrel)
                else:
                    error += 1
        return error

    def check_answer(self):
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if self.card[i][j] == barrel:
                    print('Вы проиграли!!!')
                    return 'сдаюсь'

    def check_win(self):
        win = 0
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if self.card[i][j] == '-':
                    win += 1
        return win


user_card = Card([[], [], []])
comp_card = Card([[], [], []])
barrels = [i for i in range(1, 91)]
user_answer = 0
user_card.take_card()
comp_card.take_card()

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
        if user_card.barral_in_card() == 15:
            print('Вы проиграли!!!')
            user_answer = 'сдаюсь'
        else:
            user_card.barral_in_card()
    elif user_answer.lower() == 'продолжить':
        user_answer = user_card.check_answer()
    comp_card.barral_in_card()
    if user_card.check_win() == 15:
        print('Вы выйграли!!!')
        user_answer = 'сдаюсь'
    if comp_card.check_win() == 15:
        print('Компьютер выйграл!!!')
        user_answer = 'сдаюсь'


