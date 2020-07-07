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
	t=input()
	n=len(t)
	if t.count("0")==n or t.count("1")==n:
		print(t)
	else:
		print(len(t)*"01")



