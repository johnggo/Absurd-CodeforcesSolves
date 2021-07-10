# Time: 108 ms
# Memory: 16 KB
a, b = map(int, input().split())
mi = min(a, b)
ma = max(a, b)
print(mi, (ma - mi)//2)
