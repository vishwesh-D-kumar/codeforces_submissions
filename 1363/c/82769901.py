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
	n,x=I()
	neighs=0
	for i in range(n-1):
		u,v=I()
		if u==x or v==x:
			neighs+=1
	if neighs<=1:
		print("Ayush")
	else:
		if n%2:
			print("Ashish")
		else:
			print("Ayush")

	



