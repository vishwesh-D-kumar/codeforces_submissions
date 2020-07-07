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
	l=2
	for i in range(100):
		l*=2
		if n%(l-1)==0:
			break
	# print(l)
	print(n//(l-1))



