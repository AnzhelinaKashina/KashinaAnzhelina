def alec(n ):
    if n>= 9 or n < 1:
        print("Еrrоr")
    else:
        for x in range(n):
            for y in range(1, x + 2):
                print ( y, end='' )
            print()
alec(int(input()))