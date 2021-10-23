def newString(baseStr, n):

# проверим что запрашиваем не больше символов, чем есть в строке
    if n > len(baseStr): 
        print('Invalid len')
        return ''
    
    newStr = ''
    for i in baseStr:
        b = baseStr.index(i)  
        if b < n: #набираю n символов из строки
            if i not in newStr: #проверяю чтоб не добавлялись повторяющиеся символы
                newStr += i
    return newStr

x = newString(input('введите строку '), int(input('Введите число: ')))
print(x)