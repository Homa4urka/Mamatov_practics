# Добавить в словарь новый элемент elephant = слон, если его еще нет в словаре
a = {'cat': 'кошка', 'dog': 'собака', 'bird': 'птица', 'mouse': 'мышь'}
if 'elephant' not in a:
    a['elephant'] = 'слон'
print(a)