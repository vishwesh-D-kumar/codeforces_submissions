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
	n,a,b,c,d=I()
	if n*(a+b)<(c-d) or n*(a-b)>(c+d):
		print("No")
	else:
		print("Yes")



