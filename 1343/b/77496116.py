import sys
# input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n=int(input())
	if (n//2)%2!=0:
		print("NO")
	else:
		print("YES")
		n=n//2
		a=[-1]*2*n
		se=0
		so=0
		for i in range(1,n+1):
			a[i-1]=2*i
			se+=2*i
			a[i+n-1]=2*i-1
			so+=2*i-1
		a[-1]+=se-so
		print(*a)



