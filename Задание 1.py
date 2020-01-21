#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.


my_list_1 = [ 2, 4, 6, 8, 10]
print (type( my_list_1))

my_list_2 = "Hello , i am Kseniya"
print (type( my_list_2))

s1 = "Tomsk"
print(type (s1))

print(s1 + my_list_2)
print (my_list_1 [1:3])
def my_list_2 (string):
    return string [2:3]
print(my_list_2 (" Hello, i am Kseniya"))
for el in reversed(" Hello, i am Kseniya"):
 print(el)

my_list_1.append(88)
print(my_list_1)

my_list_1.extend([1,3,5])
print(my_list_1)

my_list_1.remove(3)
print(my_list_1)

my_list_1.pop(2)
print(my_list_1)

print(tuple("Фломастер"))


my_list_3 = tuple ("компьютер")
print(my_list_3)
print(type(my_list_3))

my_list_3 = set ("Компьютер")
print(my_list_3)
print (type(my_list_3))

my_list_3.add("True")
print(my_list_3)

my_list_3.remove("True")
print(my_list_3)

my_list_4 = {"key_1": 123, 5: 300, "key_3": True, 4: None}
print(my_list_4.keys())
print(type(my_list_4))
print(my_list_4.values())
print(my_list_4.items())

for el in my_list_1:
    my_list_1.append((el * 2))
print(my_list_1)