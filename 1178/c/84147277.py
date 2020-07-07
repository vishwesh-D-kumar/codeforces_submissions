import sys
# from math import pow
input = sys.stdin.buffer.readline
def I(): return(list(map(int,input().split())))
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a

# for __ in range(int(input())):
w,h=I()
print(pow(2,w+h,998244353))




