N=int(input())
LIS=list(map(int,input().split()))
LIS1=[]
X=0
for i in range(N):
	if LIS[i] in LIS1:
		X=1
		NUM=LIS[i]
		break
	else:
		LIS1.append(LIS[i])
if(X==1):
	print(NUM)
else:
	print("unique")
