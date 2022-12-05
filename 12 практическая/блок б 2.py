def maximum():
    max1 = 0
    max2 = 0
    a=int(input('Введите элемент '))
    if a==0:
        return 0

    if a >= max1:
        max2 = max1
        max1 = max(a,maximum())
        return max1
    elif max2 < a :
        max2 = a
        return max2
print(maximum())
