import random

def returnN(n):


#наполняем список   
    newList = []
    for i in range (15):
        newList.append(random.randint(1,20))
# проверим что запрашиваем не больше символов, чем есть в строке
    if n > len(newList): 
        print('Invalid len')
        return ''
# выбираем случайные
    for y in range (n):
        random_index = random.randint(0, len(newList) - 1)
        print(newList[random_index])
    return ''
x = returnN(int(input('Введите нужное количество элементов: ')))
print(x)
