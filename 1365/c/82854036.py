import sys
input = sys.stdin.buffer.readline
from collections import Counter
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a
def check(k):
	a1=a[k:]+a[:k]
	c=0
	print(a1,b)
	for i in range(n):
		if a1[i]!=b[i]:
			c+=1
	return n-c
# for __ in range(int(input())):
n=int(input())
a=I()
b=I()
# for k in range(n):
# 	print(k,check(k))
# i=a.index(b[0])
# a=a[i:]+a[:i]
# i=b.index(1)
# b=b[i:]+b[:i]
c=0
# print(a)
# print(b)
aidxs=[-1]*(n+1)
bidxs=[-1]*(n+1)
for i in range(n):
	aidxs[a[i]]=i
	bidxs[b[i]]=i

cs=[]
for i in range(1,n+1):
	if aidxs[i]<=bidxs[i]:
		cs.append(bidxs[i]-aidxs[i])
	else:
		cs.append(n-(aidxs[i]-bidxs[i]))
# print(cs)
print(Counter(cs).most_common(1)[0][1])
# print(n-c)




