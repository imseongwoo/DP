n = int(input())

d = [-1] * 30001
d[1]=0
for i in range(2, n + 1):
    a = 9999
    b = 9999
    c = 9999
    g = 9999
    if i % 5 == 0:
        a = d[i // 5]
    elif i % 3 == 0:
        b = d[i // 3]
    elif i % 2 == 0:
        c = d[i // 2]
    g=d[i-1]
    d[i] = min(a, b, c, g) + 1

print(d[n])
