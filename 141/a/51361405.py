a=input()
b=input()
c=input()
dic={}
dic2={}


for  i in range(ord('A'),ord('Z')+1):
	dic[chr(i)]=0
	dic2[chr(i)]=0
for i in a+b :
	dic[i]+=1
for i in c:
	dic2[i]+=1

if dic==dic2:
	print("YES")
else:
	print("NO")