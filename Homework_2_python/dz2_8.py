def sumDig(num):

    result = 0
    while num > 0:
        result += num % 10
        num //= 10
    return result
 
x = sumDig(int(input('Введите число: ')))
print('сумма цифр равна ', x)