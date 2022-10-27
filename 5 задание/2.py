def asb(natd):
    i = 2
    while natd % i != 0:
        i += 1
    return i
print(asb(int(input())))