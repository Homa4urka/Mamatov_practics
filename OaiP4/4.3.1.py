#Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK .
N, K = input("Введите первое число: "), input("Введите второе число: ")
while type(N) != int: # обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input("Введите первое число: ")
while type(K) != int: # обработка исключений
    try:
        K = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = input("Введите второе число: ")
counter = 1
summa = 0
while counter <= N:
    summa = summa + K * counter
    counter += 1
print(summa)