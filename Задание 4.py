#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.


my_str = "london is a capital of great britain"
print(type (my_str))
print(my_str.split(" "))


print (my_str [0:6:1])
print(my_str [7:9:1])
print(my_str [9:11:1])
print(my_str [11:19:1])
print(my_str [19:22:1])
print(my_str [22:28:1])
print(my_str [28:36:1])



for value,index in enumerate (my_str.split(), 1):
    print(value,index)
