from collections import Counter

dlist = [[1,1,3,2],[9,8,8,1],[0,4,5,0,0,1,4]]
for x in dlist:
    for i in x:
        counts = dict(Counter(x))
        duplicates = {key: value for key, value in counts.items() if value > 1}
    for key, value in duplicates.items():
        print(f'{key} -> {value}')
