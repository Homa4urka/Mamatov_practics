#2. Дан список A размера N. Сформировать новый список B
# того же размера, элементы которого определяются следующим образом:
# BK = 2*AK, если AK < 5, AK/2 в противном случае.
N = int(input('Введите размер целочисленного списка: '))
A = []
B = []
if N <= 1:
    print('Список слишком маленький!')
else:
    for chislo in range(N):
        chislo = int(input('Введите число: '))
        A.append(chislo)
    print(A)
    for i in range(N):
        if A[i] < 5:
            B.append(A[i] * 2)
        else:
            B.append(A[i] / 2)
print(B)