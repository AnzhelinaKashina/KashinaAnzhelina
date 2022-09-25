def avcrt(n, m, k):
    if k % n == 0 or k % m == 0:
        if n * m >= k:
            return 'да'
        else:
            return 'нет'
    else:
        return 'нет'
print(avcrt(2,10,5))