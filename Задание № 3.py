# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int ( input( " Введите число"))
sym = str (n)
number1 = sym + sym
number2 = sym + sym + sym
total = n + int ( number1) + int (number2)
print ( total)
