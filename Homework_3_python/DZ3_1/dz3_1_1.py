
def readDate(filename):

     with open(filename) as f:
        data = []
        n = 0
        countNum = []  # список чисел
        countS = []
        max = 0
        min = 0
        count = 0
        n1 = 0
        for line in f:
            data.append([float(i) for i in line.split()])
        print(data)
        for i in data:
                        if i.isnumeric():
                            n += 1
                            if int(i) > int(max):
                                max = i
                            if int(i) < int(min):
                                min = i
                            count += int(i)
                            if int(i) % 2 == 0:
                                n1 += 1
        countS.append(count)
        countNum.append(n)  # количество чисел
        countSRes = sum(countS)# сумма цифр
        countNumtRes = sum(countNum)
        average = countSRes / countNumtRes
        s = str(countNumtRes)
        s1 = str(max)
        s2 = str(min)
        s3 = str(average)
        s4 = str(n1)

        print(s, n, countSRes, average, n1)

        f = open('files_output1.txt','w')  # открытие в режиме записи
        f.write('в файле ' + s + ' чисел, ' + 'наибольшее число - ' + s1 + ', наименьшее число - ' + s2 + ', среднее арифметическое - ' + s3 + ', четных чисел в файле - ' + s4)  # запись в файл
        f.close()  # закрытие файла
readDate("files_input1.txt")
