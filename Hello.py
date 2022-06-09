# S = [(11, 14), (0, 78), (33, 11), (0, 78)]

# print("The list of tuple is : ")
# print(S)

# list = list(set([i for i in S]))

# print("The list of tuples after removing duplicates is :")
#print(list)


# To print list on fruits
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

output_set = set()

# Using loop for constructing output set
for var in input_list:
	if var % 2 == 0:
		output_set.add(var)

print("Output Set using for loop:", output_set)





# To calculate Matrix
matrix = []

for i in range(5):
	
	# Append an empty sublist inside the list
	matrix.append([])
	
	for j in range(5):
		matrix[i].append(j)
		
print(matrix)



# Python3 program to calculate nPr
import math
def fact(n):
	if (n <= 1):
		return 1
		
	return n * fact(n - 1)

def nPr(n, r):
	
	return math.floor(fact(n) /
				fact(n - r))
	
# Driver code
n = 6
r = 3

print(n, "P", r, "=", nPr(n, r))





from threading import *


class Hello:
	def run(self):
		for i in range(4):
			print(f"Hello {i}")


hello = Hello()
hello.run()			





































