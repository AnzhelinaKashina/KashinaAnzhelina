def faa(n):
    sumi=2
    a =1
    b = 1

    for i in range(2,n):
        a, b = b, a + b
        sumi+=b
    return sumi
print(faa(int(input())))