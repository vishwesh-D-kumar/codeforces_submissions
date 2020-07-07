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
	a,k=I()
	a=str(a)
	mi=min(a)
	ma=max(a)
	for i in range(k-1):
		mi=min(a)
		ma=max(a)
		if mi=="0":
			break
		a=str(int(a)+int(min(a))*int(max(a)))
	print(a)

	



