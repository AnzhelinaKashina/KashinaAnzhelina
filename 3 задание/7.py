def year(a):
    if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
        return 'да'
    else:
        return 'нет'
print(year(2022))

