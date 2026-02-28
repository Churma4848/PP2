def sqrs(n, m):
    j = 0
    for i in range(n, m+1):
        yield i*i

a, b=map(int, input().split())

for i in sqrs(a, b):
    print(i)