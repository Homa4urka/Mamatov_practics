#Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
from math import factorial
summa = 0
n = int(input('Введите число:'))
for i in range(1, n+1):
    summa += factorial(i)
print(summa)