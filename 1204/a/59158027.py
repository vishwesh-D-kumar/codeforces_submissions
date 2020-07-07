import sys
s=input()
flag=True
if s=="0" or s=="1":
	print(0)
	sys.exit()
if s=="10" or s=="11" or s=="100":
	print(1)
	sys.exit(0)

if s[0]=="1":
	c=0
	for i in s[1:]:
		# print(i)
		c+=1
		if i!="0":
			flag=False
			break
	# print(c)
	if c%2!=0 and flag:
		flag=False
else:
	flag=False
# print(flag)
if flag:
	print((len(s)-1)//2)
else:
	print((len(s)-1)//2+1)