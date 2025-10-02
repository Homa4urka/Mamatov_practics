#Ввести N чисел. Посчитать и вывести количество чисел равных нулю.
N = int(input('Введите количество чисел: '))
l = []
counter = 0
for i in range(N):
    l.append(int(input("Введите число: ")))
for i in l:
    if i == 0:
        counter += 1
    else:
        continue
print('Чисел, равных нулю:', counter)