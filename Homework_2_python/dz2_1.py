def checkRemainder(a, b):
    

    if a % b == 0:
        print ('Число', a, 'делится на число', b, 'без остатка')
    else:
        print ('Число', a, 'не кратно числу', b)



checkRemainder(int(input('Введите первое число: ')), (int(input('Введите второе число: '))))