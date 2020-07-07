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
	a=input()
	b=input()
	c=input()
	n=len(a)
	ans="YES"
	for i in range(n):
		if c[i]==b[i] or c[i]==a[i]:
				continue
		ans="NO"
	print(ans)



