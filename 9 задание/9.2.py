import random
from functools import reduce
from operator import mul
def razmer(n):
    matricafff = []

    for i in range(n):
        matricafff.append([random.randint(-10, 10) for x in range(n)])
    print('исходный массив', *matricafff,sep=",\n", end="]\n")

    tarray = [list(i) for i in zip(*matricafff)] #удобный вид для меня , тут столбики в строчке )))

    proizved = [reduce(mul, row) for row in tarray]
    min_p = min(proizved)
    index = proizved.index(min_p)

    if index < n - 1:
        tarray[index], tarray[index + 1] = tarray[index + 1], tarray[index]
    else:
        tarray[index], tarray[index - 1] = tarray[index- 1], tarray[index]
    otvet = [list(i) for i in zip(*tarray)] #возвращаем в нормальный вид
    print('ответ', *otvet,sep=",\n", end="\n")
razmer(int(input('введите размер массива')))

