#Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
#в противном случае уменьшить на 2.
a = int(input("Введите число:"))
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите число: ")
astr = str(a)
b, c = astr[0], astr[1]
cint = int(c)
bint = int(b)
if (cint + bint) % 2 == 0:
    a = a + 2
else:
    a = a - 2
print(a)