while True:
    a = str(input())
    if(a == ""):
        break
    else:
        k = len(a) + 1
        flag = True
        for i in range(0, k):
            for j in range(i + 1, k):
                if(a[i] == a[j]):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            print(a)
