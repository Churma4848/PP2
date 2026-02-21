def prime(a):
    b = True
    for j in range(2, a):
        if (a % j == 0):
            b = False
            return b
    return b

def sol(num):
    for i in range(1, num + 1):
        if(num % i == 0):
            if(prime(i) == True):
                if(i != 3 or i != 3 or i != 5):
                    return False
    return True
n = int(input())
if(sol(n) == False):
    print("No")
else:
    print("Yes")