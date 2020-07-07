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
	s=input()
	x=s.find("1")
	if x==-1:
		print(0)
	else:
		y=len(s)-1-s[::-1].find("1")
		print(s[x:y+1].count("0"))

	



