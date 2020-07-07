from collections import defaultdict,Counter
n=int(input())
s=input()
x=defaultdict(list)
for i in range(len(s)):
	x[s[i]].append(i)

for ii in range(int(input())):
	y=Counter(input())
	m=max([x[i][y[i]-1]for i in y])
	print(m+1)