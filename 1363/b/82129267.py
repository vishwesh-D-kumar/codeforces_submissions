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
def check(s1,s):
	c=0
	for i in range(n):
		if s[i]!=s1[i]:
			c+=1
	return c
for __ in range(int(input())):
	s=input()
	n=len(s)
	ans=n
	s1=["0"]*n
	s2=["1"]*n
	c1=check(s1,s)
	c2=check(s2,s)
	ans=min(ans,check(s1,s),check(s2,s))
	for i in range(n):
		# s1[i]="1"
		if s[i]=="1":
			c1-=1
			c2+=1
		else:
			c2-=1
			c1+=1
		# s2[i]="0"
		# print(i,c1,c2)
		ans=min(ans,c1,c2)
	print(ans)

