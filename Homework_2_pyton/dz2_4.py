
def argmin(lst):

    min = lst[0]  # присваиваю переменной первое значение списка  

    # перебираю каждое число из списка и сравниваю с переменной min если оно меньше - перезаписываю переменную
    for a in lst: 
        if a < min: 
            min = a

    ind = lst.index(min) # узнаем индекс итогового значения переменной
    
    # все на печать
    print("the smallest number is: ", min) 
    print("the index of this namber is: ", ind)
    return

x = argmin([55, 8984, 6, 8, 7])

