def sqrs(n):
    while(n>=0):
        yield n
        n = n-1

# a, b=map(int, input().split())
a= int(input())

for i in sqrs(a):
    print(i)