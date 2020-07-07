def I():return list(map(int,input().split()))
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
maxS=1*3+2*3+3
allPosible=["100","010","001","110","011","101","111"]
s=powerset(allPosible)
sums=[]
for i in s:
	a,b,c=0,0,0
	for j in i:
		if j[0]=="1":
			a+=1
		if j[1]=="1":
			b+=1
		if j[2]=="1":
			c+=1
	sums.append([a,b,c])



for __ in range(int(input())):
	a,b,c=I()
	m=0
	for i in range(len(sums)):
		if a>=sums[i][0] and b>=sums[i][1] and c>=sums[i][2]:
			m=max(len(s[i]),m)
	print(m)





