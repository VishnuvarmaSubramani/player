N=int(input())
LIS=list(map(int,input().split()))
for i in LIS:
	if LIS.count(i)==1:
		print(i)
		break
