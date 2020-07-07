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
	t=I()
	m=max(t)
	f=True
	for i in range(n):f=f and ((m-t[i])%2==0)
	print("YES") if f else print("NO")

