def numAndLen(filename):
    with open(filename) as f:

        countLet = 0
        countWordText = []#список для слов
        countLetText = []#список для букв
        for line in f:
            varTemp = len(line.split())#количество слов в строке
            countWordText.append(varTemp)#количество слов в тексте
            for i in line:
                if i.isalpha():
                    countLet += 1#количество букв в строке
        countLetText.append(countLet)#количество букв в тексте
    countLetTextRes = sum(countLetText)
    countWordTextRes = sum(countWordText)
    c = countLetTextRes / countWordTextRes
    print(countWordTextRes, countLet, countLetTextRes)
    f = open('files_output5.txt','w')  # открытие в режиме записи
    s1 = str(c)
    s2 = str(countWordTextRes)
    f.write('в файле ' + s2 + ' слов, ' + s1 + ' средняя длина слова')  # запись в файл

    f.close()  # закрытие файла
numAndLen("files_input5.txt")