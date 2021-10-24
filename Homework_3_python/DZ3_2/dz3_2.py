
def upperAndLower(filename):
    with open(filename) as f:
        varUppTemp = [] #переменная для списка который будет заглавными
        varLowTemp = [] #переменная для списка который будет строчными
        for i in f:
            b = i.upper()
            varUppTemp.append(b)
            varUpp = str(varUppTemp)
            c = i.lower()
            varLowTemp.append(c)
            varLow = str(varLowTemp)

    f = open('files_outputUppper.txt', 'w')  # открытие в режиме записи
    f.write(varUpp)  # запись в файл

    f = open('files_outputLower.txt', 'w')  # открытие в режиме записи
    f.write(varLow)  # запись в файл

    f.close()  # закрытие файла
upperAndLower("files_input5.txt")
