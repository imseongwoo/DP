n=int(input())

array=list(map(int,input().split()))

d=[0]*100       #dp 테이블 초기화


#d[n]은 n번째에서 털 수 있는 최대 식량의 값
d[0]=array[0]
d[1]=max(array[0],array[1])
for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])
