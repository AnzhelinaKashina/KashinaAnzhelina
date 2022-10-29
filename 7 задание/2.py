def asve(k):
    akus=[]
    for i in range(k):
        print('введите', i, 'элемент:')
        akus.append(int(input()))
    print(akus)
    b=[]
    for j in range (len(akus)):
        if akus[j]%2==0 and akus[j]<10:
            b.append(akus[j])
    if len(b)==0:
        print('Таких чисел нет ')
    else:
        b.sort()
        print(b)

asve(int(input()))