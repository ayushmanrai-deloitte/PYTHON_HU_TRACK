from math import floor

row = 9
middle = floor(row/2)
for i in range(middle+1):
    for j in range(row-1):
        if j == middle:
            print('*',end='')
        if j in range(middle-i,middle+i):
            print('*', end='')
        else:
            print(' ', end='')
    print()
for i in range(row-middle-1):
    for j in range(row):
        if j in range(i+1,row-i-1):
            print('*', end='')
        else:
            print(' ', end='')
    print()