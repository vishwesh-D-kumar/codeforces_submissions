def I(): return(list(map(int,input().split())))
def sieve(n):
	p=2
	primes=[True]*(n+1)
	primes[1]=False
	primes[0]=False
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
n,m=I()
x=[]
primes=sieve(100000)
diffToNextPrime=[0]*(100001)
p=100003
for i in range(100000,-1,-1):

	if primes[i]:
		p=i

	diffToNextPrime[i]=p-i
	# print(p,i)


# print(diffToNextPrime[12049])

for i in range(n):
	x.append(I())
m=len(x[0])
ma=99999999
for i in range(n):
	s=0

	for j in range(m):
		# print(x[i][j])
		x[i][j]=diffToNextPrime[x[i][j]]
		s+=x[i][j]
	# print(*x[i])
	ma=min(s,ma)

for i in range(m):
	s=0
	for j in range(n):
		# x[j][i]=diffToNextPrime[p]
		s+=x[j][i]
	ma=min(s,ma)
print(ma)

