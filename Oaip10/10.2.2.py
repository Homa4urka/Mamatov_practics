stroka, punkts, count = '', 0, 0
f1 = open('text18-23.txt', 'r', encoding='utf-8')
for line in f1:
    while count < 4:
        count += 1
        stroka = line.strip()
        for s in stroka:
            if s in '.,:':
                punkts += 1
f1.close()
f1 = open('text18-23.txt', 'r', encoding='utf-8')
f2 = open('text18-23_new.txt', 'w', encoding='utf-8')
for line in f1:
    s = line.lower()
    f2.write(s)
f1.close()
f2.close()
print(f'Количсетво знаков препинания: {punkts}')