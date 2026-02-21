n = int(input())
m = int(input())
for i in range(n, m+1):
    a = i % 10
    b = ((i % 100) - a) / 10
    c = ((i % 1000) - 10 * b - a) / 100
    d = i // 1000
    if (a == b or b == c or a == c or a == d or b == d or c == d):
        continue
    else:
        print(i)