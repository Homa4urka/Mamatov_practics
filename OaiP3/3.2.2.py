#Вести число. Если оно четное, разделить его на 4,
#если нечетное - умножить на 5.
a = input("Введите число:")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")
if a % 2 == 0:
    print( a / 4 )
elif a % 2 == 1:
    print( a * 5 )