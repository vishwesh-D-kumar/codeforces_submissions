from collections import Counter
def I():return list(map(int,input().split()))
for __ in range(int(input())):

	n=int(input())
	s=I()
	f=0
	for i in range(n-2):
		for j in range(i+2,n):
			if s[i]==s[j]:
				f=1
				break

	print("YES") if f else print("NO")
