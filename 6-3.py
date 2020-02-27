'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
'''

dict_income = {'оклад': 120000, 'премия': 25000}


class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict_income


class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник: {self.name} {self.surname}, должность: {self.position}')

    def get_total_incom(self):
        print(self._income)
        # print(f'Оклад {self._income['оклад']}') # Не смог понять почему нельзя работать со словарем в таком виде


new_worker = Position('Алексей', 'Шельпяков', 'Программист')
new_worker.get_full_name()
new_worker.get_total_incom()
# print(dict_income['оклад']) # Здесь же все работает
