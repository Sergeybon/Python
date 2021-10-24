
def readDate(filename):
     with open(filename) as f:
        n = 0
        for line in f:
            #if line.isnumeric():
            #    print(type(line))
                n += 1
        s = str(n)
            # line = line.strip()
        print(s)

        f = open('files_output1.txt','w')  # открытие в режиме записи
        f.write('в файле ' + s + ' чисел')  # запись в файл

        f.close()  # закрытие файла
readDate("files_input1.txt")