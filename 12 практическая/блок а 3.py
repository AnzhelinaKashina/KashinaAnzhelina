def perevorot(p):
    if p>0:
        return str(p%10)+perevorot(p//10)
    else:
        return ''
print(perevorot(int(input())))