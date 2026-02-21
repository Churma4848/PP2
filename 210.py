s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(input())
d = ""
for i in range(n, n + 4):
    d = f"{d}{s[(i-1) % 26]}"
print(d)
    