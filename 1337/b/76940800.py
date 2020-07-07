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
	x,n,m=I()
	for i in range(n):
		if x<=20:break
		x=x//2+10
		
	x-=m*10
	print(["YES","NO"][x>0])





