import math

def sol(n):
    n = abs(n)
    digits =[]
    k = 0
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    for i in digits:
        if(i % 2 == 1):
            return "Not valid"
    return "Valid"


n = int(input())
print(sol(n))