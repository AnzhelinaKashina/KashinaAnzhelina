def cvc (n):
    x=1
    summa=0
    for i in range(1, n + 1):
        x *= i
        summa += x
    return summa
print(cvc(int(input())))