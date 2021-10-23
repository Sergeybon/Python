
def numDigits(n):

    i = 0
    while n > 0:
        n = n//10
        i += 1
    return i
 
x = numDigits(int(input('Введите число: ')))
print('Количество разрядов:', x)
