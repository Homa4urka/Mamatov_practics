#1. Дан целочисленный список размера N, не содержащий одинаковых чисел.
#Проверить, образуют ли его элементы арифметическую прогрессию.
#Если образуют, то вывести разность прогрессии, если нет — вывести 0.
N = int(input('Введите размер целочисленного списка: '))
spisochek = []
total = 0
if N <= 1:
    print('Список слишком маленький!')
else:
    for i in range(N):
        chislo = int(input('Введите целое число: '))
        spisochek.append(chislo)
    print(spisochek)
    raznica = spisochek[1] - spisochek[0]
    for i in range(N - 1):
        if spisochek[i + 1] - spisochek[i] == raznica:
            total = True
        else:
            total = False
            break
if total == True:
    print('Разница прогрессии: ', raznica)
else:
    print('0')