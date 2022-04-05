row = int(input('Enter number of rows : \n'))  #giving input
for i in range(row):
    print('*',end='')
print()
for i in range(1,row):  #starting loop
    for j in range(row):
        if j==i or j==row-1:
            print('*',end='')
        else:
            print(" ",end='')
    print()