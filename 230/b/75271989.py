def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
		if a[i]:
			for j in range(i*i,n,i):
				a[j]=0
			r.add(i*i)
	return a
n=2**20
r=set()
sieve(n)
input()
for a in I() :
	print (['NO','YES'][a in r])