N=int(input())
LIS=list(map(int,input().split()[:N]))
for i in range(0,N):
    if i%2==0 and LIS[i]%2!=0:
        print(LIS[i],end=" ")
    elif i%2!=0 and LIS[i]%2==0:
        print(LIS[i],end=" ")
