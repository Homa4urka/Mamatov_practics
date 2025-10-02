#Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2
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
if (a+b) % 5 == 0:
    print(a+b+1)
else:
    print(a+b-2)