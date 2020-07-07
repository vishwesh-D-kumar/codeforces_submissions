# from itertools import permutations,combinations
# import math
n=int(input())
a=range(1,n//2+1)
b=range(n//2+1,n+1)
print((n//2)*(n-(n//2)))
for i in a:
	for j in b:
		print(i,j)

