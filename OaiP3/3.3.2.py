#Вариант 23.
#2. Дано целое число. Если оно является положительным, то прибавить к нему 1;
#в противном случае вычесть из него 2. Вывести полученное число.
number = int(input("Введите число:"))
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Неправильно ввели!")
        number = input("Введите число: ")
if number > 0:
    print(number + 1)
else:
    print(number - 2)
