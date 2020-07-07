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
	s=[int(i) for i in input()]
	i=n-1
	while(i>=0):
		j=i
		if s[i]==1:
			i-=1
			continue
		while(i>=0 and s[i]==0):
			i-=1
		if i<0:
			break
		else:
			# print(j,"#")
			while(j>=0 and s[j]==0):
				s[j]=-1
				j-=1
			# print(j,"#")
			s[i]=0
	for i in range(len(s)):
		if s[i]==-1:
			continue
		print(s[i],end="")
	print()


	



