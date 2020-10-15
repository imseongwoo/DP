# n=int(input())
#
# array=list(map(int,input().split()))
#
# result=0
# for i in range(n):
#     for j in range(i+2,n):
#         result=max(result,array[i],array[i]+array[j])
#
# print(result)

#---------------------------------------------------------------
# 개미전사 dp 로 해결
n = int(input())
array = list(map(int,input().split()))

d=[-1]*1001

d[0] = array[0]
d[1] = max(array[0],array[1])

max_num = d[1]
for i in range(2,n):
    d[i] = max((array[i]+array[i-2]),array[i-1])

    if d[i]>max_num:
        max_num = d[i]

print(max_num)