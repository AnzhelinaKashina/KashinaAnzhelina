def ghd(k):
    m=0
    sumar=0
    while k!=0:
        k=int(input("Введите люое число \n "))
        if k==0:
            break
        m += 1
        sumar+=k
    print(sumar/m)
ghd(9)