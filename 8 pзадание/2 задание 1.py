a = [5, 6, 7, 8, 2, 3] # у меня маленькая матрица,да и вообще, матрицы только с 9 практической
b = [5, 6, 7, 8, 2, 7, 12]  #а это только 8 практическая и поэтому матрицу задам руками!!

def func():
    print(a)
    print(b)

    c = 0
    d = 0

    for i in range (len(a)):
        if c < a[i]:
            c=i

    for j in range (len(b)):
        if d < b[j]:
            d=j

    x=a[c]
    a[c]=b[d]
    b[d] = x
    print(a)
    print(b)
func()


