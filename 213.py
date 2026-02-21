s = []
while True:
    n = int(input())
    if (n == 0):
        break
    else:
        s.append(n)
print(len(s))
r = []
for i in s:
    if(i % len(s) == 0):
        r.append(i)
print(r)