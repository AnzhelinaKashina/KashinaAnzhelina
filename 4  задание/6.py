def acv(n):
    proizved=1
    for i in range (1,n+1):
        proizved*=i
    return proizved
print(acv(int(input())))
