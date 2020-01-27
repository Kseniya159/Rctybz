#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.

# а)

from itertools import count
res = []
for el  in count(10):
    if el > 20 :
        break
    res.append(el)
print(res)

#б)


from itertools import cycle

res = 0
for el  in cycle("Python"):
    if res > 6 :
        break
    print(el)
    res += 1











