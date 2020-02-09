# Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"Date ({self.day} {self.month} {self.year})"

    @classmethod
    def my_method (cls, date_str):
        day, month, year = map(int, date_str.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def date_valid(date_str):
        day, month, year = map(int, date_str.split('-'))
        return day <= 31 and month <= 12 and year <= 2022

res = Date.my_method("08-02-2020")
print(res)
date_1 = Date.date_valid("08-02-2020")
print(date_1)