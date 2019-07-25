N,K=map(int,input().split())
LIS=list(map(int,input().split()))
for j in LIS:
    if(j==K):
        print("Yes")
        break
else:
    print("No")
