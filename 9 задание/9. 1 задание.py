def matris (n):
<<<<<<< HEAD

=======
>>>>>>> 0c25beffe0da16d17745148bc206e1088e14d68e
    a=[]
    for i in range(n):
        b=[]
        for i in range(n):
            b.append(int(input('введите элементы массива')))
        a.append(b)
    for i in range(n):
        for j in range(n):
            print(a[i] [j],end='     ')
        print()
    min_a = min(sum(a,[]))
    ind_min = sum(a,[]).index(min_a) // len(a)
    print('строка с минимальным элементом: ', ind_min + 1)
    print(sum(a[ind_min]))
matris(int(input('введите количество столбцов ')))
