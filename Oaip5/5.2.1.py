#Даны три целых числа. Определить у какого числа больше сумма цифр.
#Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.
def summa(n):
    total = 0
    n = abs(n)
    while n > 0:
        total += n % 10
        n //= 10
    return total
def main():
    numbers = []
    for i in range(3):
        num = int(input(f"Введите {i+1}-е число: "))
        numbers.append(num)
    sums = [summa(num) for num in numbers]
    max_sum = max(sums)
    result = numbers[sums.index(max_sum)]
    print(f"Число с наибольшей суммой цифр: {result}")
if __name__ == "__main__":
    main()