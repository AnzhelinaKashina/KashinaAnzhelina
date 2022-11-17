def matris (n):
    with open('', 'r') as f:
        matricafff = [[int(num) for num in line.split(',')] for line in f]
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