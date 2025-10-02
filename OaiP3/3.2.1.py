#Ввести 2 числа. Если их произведение отрицательно, умножить его на 8,
#в противном случае увеличить его в 1.5 раза.
a, b = input("Введите первое число:"), input("Введите второе число:")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")
if a * b < 0:
    print(a * b * 8)
else:
    print(a * b * 1.5)