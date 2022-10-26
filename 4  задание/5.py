def abb(n):
    s=0
    for i in range (1,n+1):
        s+= i**3
    return s
print(abb(int(input())))


