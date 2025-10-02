#Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных чисел.
l = []
for i in range(4):
    l.append(input("Введите число: "))
counter = 0
summa = 0
for i in l:
    i = int(i)
    if i < 0:
        counter += 1
        summa += i
    else:
        continue
print(counter, 'отрицательных числа')
print('Сумма отрицательных чисел - ', summa)