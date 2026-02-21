n = int(input())
m = int(input())
c = f"{n}"
for i in range(n, 32, m):
    if (i == n):
        continue
    c = c + " " + str(i)
print(c)
