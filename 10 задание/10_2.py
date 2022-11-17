import random
from functools import reduce
from operator import mul
def razmer(n):
 #   matricafff = []
#
 #   for i in range(n):
  #      matricafff.append([random.randint(-10, 10) for x in range(n)])
   # print('исходный массив', *matricafff,sep=",\n", end="]\n")
    with open('КАО_у-222_vvod2зад.txt', 'r') as f:
        matricafff = [[int(num) for num in line.split(',')] for line in f]
    #print(*matricafff,sep=",\n", end="\n")
    tarray = [list(i) for i in zip(*matricafff)] #удобный вид для меня , тут столбики в строчке )))

    proizved = [reduce(mul, row) for row in tarray]
    min_p = min(proizved)
    index = proizved.index(min_p)

    if index < n - 1:
        tarray[index], tarray[index + 1] = tarray[index + 1], tarray[index]
    else:
        tarray[index], tarray[index - 1] = tarray[index- 1], tarray[index]
    otvet = [list(i) for i in zip(*tarray)] #возвращаем в нормальный вид


    with open("КАО_у-222_vivod2зад.txt", "w") as file:
        print(*otvet, file=file, sep=",\n", end="\n") # вывод в файл

    #print('ответ', *otvet,sep=",\n", end="\n")
#razmer(int(input('введите размер массива')))

razmer(1)