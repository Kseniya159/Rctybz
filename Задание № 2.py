#  Пользователь вводит время в секундах.
#  Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#  Используйте форматирование строк.

second = int (input("Введите время"))
hours = (( second //3600))%24
minuts = ( second //60)%60
second1 = second%60
print( '%d:%02d:%02d'% (hours, minuts, second1) )