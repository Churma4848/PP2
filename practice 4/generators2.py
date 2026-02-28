def even(n):
    j = 0
    while(j<=n):
        yield j
        j = i+2

n=int(input())
list = []
for i in even(n):
    if(i!= 0):
        print(",", end = "")
    print(i,end ="")