import random
chet_proiz, ne_chet_colvo, minimum, ne_chet_sum, number = 1, 1, 100, 0, 0
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
f3.write('Четные элементы: \n')
for line in f1:
    number = int(line.strip())
    if number % 2 == 0:
        f3.write(line)
        chet_proiz = chet_proiz * number
    if number < minimum:
        minimum = int(line)
if chet_proiz == 1:
    chet_proiz = 0
f3.write('Произведение четных элементов: \n')
f3.write(str(chet_proiz) + '\n')
f3.write('Минимальный элемент: \n')
f3.write(str(minimum) + '\n')
f3.write('Второй файл: \n')
f3.write('Нечетные элементы: \n')
for line in f2:
    number = int(line.strip())
    if number % 2 == 1:
        f3.write(line)
        ne_chet_colvo += 1
        ne_chet_sum =  ne_chet_sum + number
f3.write('Количество нечетных элементов: \n')
f3.write(str(ne_chet_colvo) + '\n')
f3.write('Сумма нечетных элементов: \n')
f3.write(str(ne_chet_sum) + '\n')
f3.close()
f3 = open('results.txt', 'r', encoding='utf-8')
print(f3.read())