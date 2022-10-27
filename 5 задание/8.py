def ghd(k):
    maxim=1
    c=1
    while k!=0:
        b=k
        k=int(input())
        if k==b:
            c+=1
        elif c>maxim:
            maxim=c
            c=1
        else:
            c=1
    print(maxim)
ghd(int(input()))