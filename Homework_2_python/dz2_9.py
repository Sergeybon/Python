def cutStr(testStr):
# отделяем слева и справа куски строки до разделителя "h"
    a = testStr.partition('h')
    b = testStr.rpartition('h')
# выбираем нужные первую и последние части из списков
    a1 = a[0]
    b1 = b[-1]
# склеиваем обе части 
    a1 += b1
    return a1
 
x = cutStr('beforehlkhklgliuhhljphafter')
print(x)