import sys
input = sys.stdin.buffer.readline
from math import log2
def I(): return(list(map(int,input().split())))
def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
def sieve(n):
	a=[1]*n
	for i in range(2,n):
	    if a[i]:
	        for j in range(i*i,n,i):
	            a[j]=0
	return a
def calc(n):
	c=0
	while(True):
		if n%2:break
		c+=1
		n//=2
	return c
# primes=sieve(10**9)
for __ in range(int(input())):
	n=int(input())
	ans=["Ashishgup","FastestFinger"]
	f=0
	if n==1:
		f=1
	elif n==2:
		f=0
	elif n%2:
		f=0
	elif calc(n)==1:
		if isPrime(n//2):
			f=1
		else:
			f=0
	elif 2**calc(n)==n:
		f=1
	else:
		f=0
	print(ans[f])


