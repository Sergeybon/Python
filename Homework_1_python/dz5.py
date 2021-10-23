
'''
#то что закоментировано я сам сделал, оно работает, а то ниже закомментированной области - подсмотрел в интернете

a = str (input ('введите строку: '))
n = 0
for i in a:
    if i =="a":
        n = n+1
    elif i =="A":
        n = n+1
        
    elif i =="o":
        n = n+1
    elif i =="O":
        n = n+1
    elif i =="e":
        n = n+1
    elif i =="E":
        n = n+1
    elif i =="i":
        n = n+1
    elif i =="I":
        n = n+1
    elif i =="u":
        n = n+1
    elif i =="U":
        n = n+1
    elif i =="y":
        n = n+1
    elif i =="Y":
        n = n+1
        

print ('гласных букв в строке ', n)

'''


stroka = str (input ('введите строку: '))
#обнуляем счетчик
schetchik = 0
#задаем множество гласных
glasnie = set ("aoeiuyAOEIUY")
#проверяем каждую букву строки относится ли она к нашему множеству
for simvol in stroka:
    if simvol in glasnie:
#добавляем 1 к счетчику за каждую относящуюся к множеству
        schetchik = schetchik+1
            
print ('гласных букв в строке ', schetchik)
