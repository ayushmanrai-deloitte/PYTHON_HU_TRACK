num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
def decorate(func):
    def twice(n1, n2):
        func(n1, n2)
        return func(n1, n2)
    return twice
@decorate
def multiply(num1, num2):
    print(num1 * num2)
multiply(num1, num2)