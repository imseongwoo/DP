n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(int(input()))
d=[10001]*101

d[0]=0

for i in range(1,m+1):
    for j in range(n):
        if array[j] == i:
            d[i]=1

        if d[i] != 10001:
            d[i+array[j]]=min(d[i]+1,d[i+array[j]])
if d[i]==10001:
    print('-1')
else:
    print(d[m])



