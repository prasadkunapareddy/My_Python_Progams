a = int(input("enter a value: "))
sum=0
def add(x):
    global sum
    if(x>0):
        r=x%10
        sum=10*sum+r
        return add(x//10)
    else:
        return sum
print(add(a))
    
        