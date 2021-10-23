import random

def get_pow(n):
    newList = []

    # наполняем список рандомными числами для разнообразия т.к. в задании не указано что функция должна принимать последовательность от пользователя
    for i in range (15):
        newList.append(random.randint(1,10))


    # вычисляем степень каждого числа из списка
    for a in newList:
        b = a**n
        print(a, "в степени", n, "равно ", b)


get_pow(int(input('Введите степень: ')))
