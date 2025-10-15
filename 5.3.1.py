def ramka(stroka):
    dlina = int(len(stroka))
    print('_' * (dlina + 4))
    print('|', stroka, '|', sep=' ')
    print('_' * (dlina + 4))
stroka = str(input('Введите слово: '))
ramka(stroka)