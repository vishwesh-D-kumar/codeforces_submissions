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
# def rec(l,r,i):
# 	if r>=l:return 
# 	else:
# 		if (r-l+1)%2==0:
# 			a[(r+l)//2]=c
# 			c=rec(rec(l,(r+l)//2,c+1))
# 			c=rec((r+l)//2+1,r,c+1)
# 		else:
			# c=rec()
for __ in range(int(input())):
	n=int(input())
	s=0
	for i in range(1,(n-1)//2+1):
		s+=(i*8*i)
	print(s)

	



