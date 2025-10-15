#Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.
def colvo(n):
    total = 0
    while n > 0:
        total += 1
        n //= 10
    return total
n = int(input('Введите число: '))
print(colvo(n))