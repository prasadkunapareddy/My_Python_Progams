import math
def fact(n):
    return math.factorial(n)
def calling_function():
    n=int(input("enter a number"))
    rvalue= fact(n)
    print(f"Factorial of {n} is {rvalue}")    