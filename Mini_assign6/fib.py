input_=int(input("Enter number for Fibonacci sequence: \n"))
def fib(n):
    x, y = 0, 1
    for i in range(n):
        yield x
        x, y = y, x+y
print(list(fib(input_)))
