import random

def lookForElement(n):
    newList = []

    for i in range (15):
        newList.append(random.randint(1,20))
    
    for a in newList:
        if a % n == 0:
            print(a, "кратно", n)
    


lookForElement(int(input('Введите число: ')))