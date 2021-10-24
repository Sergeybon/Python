def numAndLen(filename):
    with open(filename) as f:
        c = 0
        d = 0
        var = []#переменная для слов
        var2 = []#переменная для букв
        for line in f:
            varTemp = len(line.split())#количество слов в строке
            var.append(varTemp)#количество слов в тексте
            for i in line:
                if i.isalpha():
                    d += 1#количество букв в строке
        var2.append(d)#количество букв в тексте
    e = sum(var2)
    f1 = sum(var)
    c = e / f1
    print(f1, d, c)
    f = open('files_output5.txt','w')  # открытие в режиме записи
    s1 = str(c)
    s2 = str(f1)
    f.write('в файле ' + s2 + ' слов, ' + s1 + ' средняя длина слова')  # запись в файл

    f.close()  # закрытие файла
numAndLen("files_input5.txt")