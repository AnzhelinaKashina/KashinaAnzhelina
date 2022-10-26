def faa(n,k):
    sumi=2
    a =1
    b = 1
    for i in range(n,n+k):
        a, b = b, a + b
        print(b,sep='#')
        sumi+=b
    return sumi
print(faa(2,5))#как вообще можно сделать эту программу,сломала себе всю голову и ничего не вышло
