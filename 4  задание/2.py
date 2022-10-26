def add(a,b):
    if a<b:
        for i in range (a,b):
            print(i)
        return i+1
    if a>b:
        for i in range (a,b,-1):
            print(i)
        return i-1
print (add(int(input()),int(input())))

