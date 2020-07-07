import sys
def I(): return(list(map(int,input().split())))

def sieve(n):
	p=2
	primes=[True]*(n+1)
	while(p*p<=n):
		if primes[p]:
			         #    // Update all multiples of p greater than or  
            # // equal to the square of it 
            # // numbers which are multiple of p and are 
            # // less than p^2 are already been marked.
			for i in range(p*p,n+1,p):

				primes[i]=False
		p+=1
	return primes

r,c=I()
a=[[0 for i in range(r)]for j in range(c)]
if r==1 and c==1: 
	print(0)
	sys.exit(0)
a[0][0]=2
d=2
# f=2
f=0
if r==1:
	for i in range(c):
		a[i][0]=i+2
	f=1

if c==1:
	for i in range(r):
		a[0][i]=i+2
	f=1
	# f=1
# print(a[i][j],end=" ")
if not f:
	for j in range(c):
		for i in range(r):
			a[j][i]=(i+1)*(r+j+1)

for i in range(r):
	for j in range(c):
		print(a[j][i],end=" ")
	print()

	




