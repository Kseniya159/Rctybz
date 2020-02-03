# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
class Worker:
    def __init__(self, worker_name, worker_surname, worker_position, worker_income):
        self.worker_name=worker_name
        self.worker_surname = worker_surname
        self.worker_position = worker_position
        self._worker_income = worker_income
worker_income = {"wage": 15000, "bonus": 5000}
class Position (Worker):

    def get_full_name (self):
            return self.worker_name + ' ' + self. worker_surname + ' '+ self. worker_position
    def get_total_income (self):
            return worker_income.get ("wage") + worker_income.get ("bonus")

p = Position ("Ксения","Иванова", "инженер", worker_income)

print(p.get_full_name())
print(p.get_total_income())
