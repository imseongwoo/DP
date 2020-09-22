n=int(input())

array=list(map(int,input().split()))

result=0
for i in range(n):
    for j in range(i+2,n):
        result=max(result,array[i],array[i]+array[j])

print(result)