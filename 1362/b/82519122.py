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
	arr=I()
	s1=set(arr)
	ans=-1
	for j in range(1,1025):
		s=set()
		for i in range(n):
			s.add(arr[i]^j)
		if s==s1:
			ans=j
			break
	print(ans)








