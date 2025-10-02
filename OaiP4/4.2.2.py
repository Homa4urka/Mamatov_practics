#Ввести 4 числа. Найти и вывести на экран количество четных чисел.
l = []
for i in range(4):
    l.append(input("Введите число: "))
counter = 0
for i in l:
    i = int(i)
    if i > 0:
        counter += 1
    else:
        continue
print(counter, 'положительных чисел')