#def nFile(testFile):

with open('files_input5.txt') as f:
    c = 0
    for line in f:
        var = len(line.split())
        d = 0
        for i in line:
            if i.isalpha():
                    #print(type(i))
                d += 1
    c = d / var

    print(var, d, c)
    f = open('files_output5.txt','w')  # открытие в режиме записи
    s1 = str(c)
    s2 = str(var)
    f.write('в файле ' + s2 + ' чисел, ' + s1 + ' средняя длина слова')  # запись в файл

f.close()  # закрытие файла
#nFile(files_input5.txt)