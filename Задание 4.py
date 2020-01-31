# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#Задание сделано с помощью наставника.
from functools import reduce
my_dict = {'One' : 'один',
           'Two' : 'два',
           'Three' : 'три',
           'Four' : 'четыре'}
new_list = []
with open ("text.txt", "r") as f:
    read_file = f.read()
    lines = read_file.split('/n')
    for line in lines:
        print(reduce(lambda x, y: x.replace(y, my_dict[y]), my_dict, line))
        new_list.append(reduce(lambda x, y: x.replace(y, my_dict[y]), my_dict, line) + '\n')

with open('text_new.txt', 'w+') as new_f:
    for sublist in new_list:
        new_f.write(sublist)