def vbd(k):
    n = 0
    stepenp = 1
    while (stepenp * 2) < k:
        n += 1
        stepenp *= 2
    print(n,stepenp, sep='\n')
vbd(int(input())) #я только сейчас узнала ,что функцию можно было написать без return))