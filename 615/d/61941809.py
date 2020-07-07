def I():
	return list(map(int,input().split()))
from collections import Counter
input()
x=Counter([i%1000000007 for i in I()])
num_divisors=1
n=1
sqrt=1
for prime in x:
	num_divisors*=(x[prime]+1)
	n*=pow(prime,x[prime])%1000000007
	sqrt*=pow(prime,x[prime]//2)%1000000007
# print(num_divisors,n)
if num_divisors%2==0:
	print(pow(n,num_divisors//2,1000000007))
else:
	# print(n**0.5)
	print(pow(sqrt,num_divisors,1000000007))
