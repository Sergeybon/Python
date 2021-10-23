#def nFile(testFile):
def upperAndLower(filename):
    with open(filename) as f:

        for i in f:
            varUpp = i.upper()
            newStr = '' 
            for i in baseStr:
                b = baseStr.index(i)
                if b < n:  # набираю n символов из строки
                    if i not in newStr:  # проверяю чтоб не добавлялись повторяющиеся символы
                        newStr += i
            return newStr

            varLow = i.lower()

    f = open('files_outputUppper.txt', 'w')  # открытие в режиме записи
    f.write(varUpp + '\n')  # запись в файл
    f = open('files_outputLower.txt', 'w')  # открытие в режиме записи
    f.write(varLow + '\n')  # запись в файл

    f.close()  # закрытие файла
upperAndLower("files_input5.txt")
