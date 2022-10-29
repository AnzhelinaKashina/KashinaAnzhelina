def pocl(k):
    posled_podr_n=0
    max_posled_podr_n=0
    for i in range(len(k)):
        if k[i]=="н":
            posled_podr_n+=1
        else:
            if posled_podr_n > max_posled_podr_n:
                max_posled_podr_n=posled_podr_n
            posled_podr_n=0
    print(max_posled_podr_n)
    k=k.replace('!','.')
    print(k)
pocl(str(input()))