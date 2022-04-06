def count(list):
    Acount =0
    acount =0
    for i in list:
        for j in i:
            if j == 'A':
                Acount += 1
            if j == 'a':
                acount += 1
    return Acount, acount


lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

result = map(count,lst1)
print(list(result))