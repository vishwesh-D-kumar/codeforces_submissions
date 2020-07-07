import sys
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

for __ in range(int(input())):
	n,k=I()
	a=I()
	b=I()
	a.sort()
	b.sort(reverse=True)
	i=0
	while(i<n and a[i]<b[i] and i<k):i+=1
	print(sum(b[:i])+sum(a[i:]))



