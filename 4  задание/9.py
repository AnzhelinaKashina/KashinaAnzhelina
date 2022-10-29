def faa(n):
    sumi=0
    a =1
    b = 0

    for i in range(n):
        b,a= a + b,b
        sumi+=b
    return sumi
print(faa(int(input())))