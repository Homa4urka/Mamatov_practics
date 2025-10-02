#Вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел.
N = int(input('Введите число больше 3: '))
counter = 0
fib1, fib2 = 0, 1 #fib1 - первое число, fib2 - второе
print(fib1)
print(fib2)
for i in range(2, N):
    fib_next = fib1 + fib2
    print(fib_next)
    if fib_next % 2 == 0:
        counter += 1
    fib1, fib2 = fib2, fib_next
print('Четных чисел: ', counter)