n = int(input())
d=[9999999]*5001

arr=[3,5]
d[3]=1
d[5]=1
for i in range(2):
    for j in range(6,n+1):
        if d[j-arr[i]] != -1:
            d[j]=min(d[j],d[j-arr[i]]+1)
if d[n]==9999999:
    print(-1)
else:
    print(d[n])