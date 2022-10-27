def ghd(k):
    k=int(input())
    m=0
    while k!=0:
        k1 = int(input())
        if k!=0 and k<k1:
            m+=1
        k=k1
    print(m)
ghd(9)