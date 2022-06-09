import math

n = int(input("enter a number: "))

sum = 0

for i in range(1,n+1):
    r = i**i
    g = math.factorial(i)
    sum = sum+r/g
print(sum)    
    