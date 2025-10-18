#3. Дано множество A из N точек (точки заданы своими координатами x, у).
# Среди всех точек этого множества, лежащих в первой или третьей четверти, найти точку, наиболее близкую к началу координат.
# Если таких точек нет, то вывести точку с нулевыми координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле: R = √(x2 – x1)2 + (у2 – y1)2.
# Для хранения данных о каждом наборе точек следует использовать по два списка:
# первый список для хранения абсцисс, второй — для хранения ординат.
import math
N = int(input('Введите количество точек: '))
A = set()
for i in range(N):
    print(f"Точка {i + 1}:")
    x = float(input("  x = "))
    y = float(input("  y = "))
    A.add((x, y))
print("\nМножество точек A:")
for point in A:
    print(f"({point[0]}, {point[1]})")
min_distance = float('inf')
closest_point = (0, 0)
for point in A:
    x, y = point
    if (x > 0 and y > 0) or (x < 0 and y < 0):
        distance = math.sqrt(x ** 2 + y ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_point = (x, y)
print(f"\nРезультат:")
if min_distance != float('inf'):
    print(f"({closest_point[0]}, {closest_point[1]})")
else:
    print("(0, 0)")