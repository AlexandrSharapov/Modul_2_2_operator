#Задача "Все ли равны?":

first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
thirdint = int(input("Введите третье число: "))


#(из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

if first == second and first == thirdint : #если 1 и 2 и 3 число равны
    print('3')
elif first == second or second == thirdint or first == thirdint :  #Если 2 из 3 введённых чисел равны между собой, то 2
    print('2')
else:
    print('0')

#Если равных чисел среди 3-х вообще нет, то вывести 0