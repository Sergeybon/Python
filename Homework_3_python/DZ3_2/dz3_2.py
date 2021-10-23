#def nFile(testFile):
def upperAndLower(filename):
    with open(filename) as f:
        c = 0
        for line in f:
            varUpp = line.upper()
            f = open('files_outputUppper.txt', 'w')  # открытие в режиме записи
            f.write(varUpp + '\n')  # запись в файл
            varLow = line.lower()
            f = open('files_outputLower.txt', 'w')  # открытие в режиме записи
            f.write(varLow + '\n')  # запись в файл


    f.close()  # закрытие файла
upperAndLower("files_input5.txt")
