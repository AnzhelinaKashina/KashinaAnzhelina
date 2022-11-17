with open('фио.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f]
print(l)