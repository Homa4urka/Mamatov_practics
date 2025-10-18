#6 Программа генерирует сто случайных вещественных чисел и заполняет ими список.
# Выводит получившийся список на экран по десять элементов в ряд.
# Далее сортирует список с помощью метода sort() и снова выводит его на экран по десять элементов в строке.
# Для вывода списка использована отдельная функция, которая в качестве аргумента принимает список.
import random
def PrintList(d):
    i = 0
    while i < 100:
        if (i % 10 != 0) or (i == 0):
            print(d[i], end=' ')
        else:
            print()
            print(d[i], end=' ')
        i += 1
    print()
ListAppend = []
t = 0
while t < 100:
    ListAppend.append(round(random.random(), 2))
    t += 1
print('Исходный список', sep='\n')
PrintList(ListAppend)
ListAppend.sort()
print('Отсортированный список', sep='\n')
PrintList(ListAppend)