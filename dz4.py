a = int (input ('введите первый коэффициент: a= '))
b = int (input ("введите второй коэффициент: b= "))
c = int (input ("введите третий коэффициент: c= "))

D = b ** 2 - 4 * a * c

print("D =", D)
 
if D > 0:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("x1 =", x1, "x2 =", x2)
elif D == 0:
    x = -b / (2 * a)
    print("x =", x)
else:
    print("Корней нет")

