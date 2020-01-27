# Реализовать скрипт,
# в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
script_name ,production , rate, priz = argv
print("Имя скрипта:", script_name)
print("Выработка в часах:", production)
print("Ставка в часах:", rate)
print("Премия:", priz)
salary = (float(production) * float(rate)) + float(priz)
print(salary)