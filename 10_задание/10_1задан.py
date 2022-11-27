def matris (n):
    with open('КАО_у-222_vvod1зад.txt', 'r') as f:
        a = [[int(num) for num in line.split(',')] for line in f]
    print(a)
    #a=[]
    #for i in range(n):
     #   b=[]
      #  for i in range(n):
       #     b.append(int(input('введите элементы массива')))
        #a.append(b)
    #for i in range(n):
     #   for j in range(n):
      #      print(a[i] [j],end='     ')
       # print()
    min_a = min(sum(a,[]))
    ind_min = sum(a,[]).index(min_a) // len(a)

    indf=(sum(a[ind_min]))

    with open("КАО_у-222_vivod1зад.txt", "w") as file:
        print('строка с минимальным элементом',ind_min+1,'сумма элементов этой строки',indf, file=file, sep=",\n", end="\n") # вывод в файл
matris(1)