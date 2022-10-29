def spis(k):
    a=[]
    del_two=0
    max_del_two=0
    for i in range (k):
        print('введите',i,'элемент:')
        a.append(int(input()))
    print(a)
    for j in range (k) :
        if a[j]%2==0:
            del_two=a[j]
            if del_two > max_del_two:
                max_del_two = del_two
            del_two = 0
    print(max_del_two)
spis(int(input()))