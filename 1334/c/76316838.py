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
	n=int(input())
	s=0
	a=[0]*n
	b=[0]*n
	extraForStart=10000000000000
	for i in range(n):
		a[i],b[i]=I()
	for i in range(n):
		s+=max(0,a[i]-b[i-1])
		extraForStart=min(extraForStart,a[i]-max(0,a[i]-b[i-1]))
	print(s+extraForStart)






