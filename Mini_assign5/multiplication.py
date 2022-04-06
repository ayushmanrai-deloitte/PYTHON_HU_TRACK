from functools import reduce

n=[1,2,3,4]
print(reduce(lambda x,y:x*y,n))