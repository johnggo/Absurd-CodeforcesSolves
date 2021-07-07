# Time: 109 ms
# Memory: 12 KB	
n, k = map(int, input().split())
tl = 240 - k
pcs = 0
while tl >= (5*(pcs + 1)):
	pcs += 1
	tl -= 5*pcs
print(min(n, pcs))
