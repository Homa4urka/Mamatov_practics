import random
colvo_otric, colvo_poloj, sum_poloj, sred_arif, number = 0, 0, 0, 0, 0
N = int(input('Введите количество чисел в первом файле: '))
K = int(input('Введите количество чисел во втором файле: '))
f1 = open('first_file.txt', 'w', encoding='utf-8')
for i in range(N):
    number = random.randint(-100, 100)
    f1.write(str(number) + '\n')
f1.close()
f2 = open('second_file.txt', 'w', encoding='utf-8')
for i in range(K):
    number = random.randint(-100, 100)
    f2.write(str(number) + '\n')
f2.close()
f3 = open('results.txt', 'w', encoding='utf-8')
f1 = open('first_file.txt', 'r', encoding='utf-8')
f2 = open('second_file.txt', 'r', encoding='utf-8')
f3.write('Первый файл: \n')
f3.write('Отрицательные элементы: \n')
for line in f1:
    number = int(line.strip())
    if number < 0:
        f3.write(line)
        colvo_otric += 1
        sred_arif += number
sred_arif = sred_arif / colvo_otric
f3.write('Количество отрицательных элементов: \n')
f3.write(str(colvo_otric) + '\n')
f3.write('Среднее арифметическое: \n')
f3.write(str(sred_arif) + '\n')
f3.write('Второй файл: \n')
f3.write('Положительные элементы элементы: \n')
for line in f2:
    number = int(line.strip())
    if number > 0:
        f3.write(line)
        colvo_poloj += 1
        sum_poloj =  sum_poloj + number
f3.write('Количество положительных элементов: \n')
f3.write(str(colvo_poloj) + '\n')
f3.write('Сумма положительных элементов: \n')
f3.write(str(sum_poloj) + '\n')
f3.close()
f3 = open('results.txt', 'r', encoding='utf-8')
print(f3.read())