def adcd(a,b,c):
    if a == b == c:
        return (3)
    elif a == b or b == c or a == c:
        return (2)
    else:
        return (0)
print(adcd(100,100,100))