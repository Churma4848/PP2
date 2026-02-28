def sqrs(n):
    ans =1
    while(ans<=n):
        yield ans*ans
        ans=ans+1
n=int(input())
for i in sqrs(n):
    print(i)
