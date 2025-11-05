# Программа преобразует в словарь значения из строки
student = {}
inf = 'Иванов Иван Иванович ПОКС-29 5 3 5 5 4'
inf = inf.split()
student['Фамилия'] = inf[0]
student['Имя'] = inf[1]
student['Отчество'] = inf[2]
student['Группа'] = inf[3]
student['Оценки'] = []
for i in inf[4:]:
    student['Оценки'].append(int(i))
print(student)