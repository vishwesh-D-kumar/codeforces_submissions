import sys
# input = sys.stdin.buffer.readline
from collections import Counter
sys.setrecursionlimit(1000000)
def I(): return(list(map(int,input().split())))


# for __ in range(int(input())):
s=input()
n=len(s)
ab=[]
ba=[]
for i in range(n-1):
	if s[i:i+2]=="AB":
		ab.append(i)
	if s[i:i+2]=="BA":
		ba.append(i)
# arr="".join([str(i) for i in arr])
if ba and ab and (abs(ba[-1]-ab[0])>1 or abs(ab[-1]-ba[0])>1):
	print("YES")
else:
	print("NO")

		